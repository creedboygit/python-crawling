# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: emailhunter.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import sys
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from crawler_ui import Ui_Form
from data_manager import DataManager
from server_communication import ServerCommunication
from login import LoginWindow
import requests
import json
import time
import re
import os
from datetime import datetime, timedelta
import pandas as pd
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl

class CrawlThread(QThread):
    log_signal = Signal(str)
    finished_signal = Signal()
    started_signal = Signal(bool)

    def __init__(self, cafe_name, max_crawl_count, one_year_only):
        super().__init__()
        self.cafe_name = cafe_name
        self.max_crawl_count = max_crawl_count
        self.one_year_only = one_year_only
        self.crawling_active = True
        self.writer_data = {}
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 'Referer': 'https://cafe.naver.com/'}

    def run(self):
        self.log_signal.emit('크롤링 시작')
        url = f'https://cafe.naver.com/{self.cafe_name}'
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            self.log_signal.emit('카페 페이지 접근 성공')
        except requests.exceptions.RequestException as e:
            self.log_signal.emit(f'카페 페이지 접근 실패: {e}')
            self.started_signal.emit(False)
            return None
        else:
            match = re.search('clubid=([a-zA-Z0-9_-]+)', response.text)
            if not match:
                self.log_signal.emit('세부정보를 찾을 수 없음')
                return
            club_id = match.group(1)
            self.log_signal.emit('카페정보 추출 성공')
            initial_article_id = self.get_initial_article_id(club_id)
            if not initial_article_id:
                self.log_signal.emit('최초 게시물 번호를 찾을 수 없음')
                return
            self.started_signal.emit(True)
            crawl_limit = max(0, initial_article_id - self.max_crawl_count)
            self.log_signal.emit(f'크롤링 시작 - 최대 {self.max_crawl_count}개의 게시물 크롤링')
            start_time = time.time()
            while self.crawling_active:
                self.log_signal.emit(f'현재 번호: {initial_article_id}, 목표 번호: {crawl_limit}')
                if not self.crawl_articles(club_id, initial_article_id, crawl_limit):
                    break
            end_time = time.time()
            elapsed_time = end_time - start_time
            self.log_signal.emit(f'크롤링 완료 - 소요 시간: {elapsed_time:.2f} 초')
            self.finished_signal.emit()

    def get_initial_article_id(self, club_id):
        self.log_signal.emit('최초 게시물 번호 검색 시도')
        url = f'https://apis.naver.com/cafe-web/cafe2/ArticleListV2dot1.json?search.clubid={club_id}&search.queryType=lastArticle&search.page=1&search.perPage=1'
        response = requests.get(url, headers=self.headers)
        data = response.json()
        article_list = data.get('message', {}).get('result', {}).get('articleList', [])
        if article_list:
            self.log_signal.emit(f"최초 게시물 번호 검색 성공: {article_list[0].get('articleId')}")
            return article_list[0].get('articleId')
        self.log_signal.emit('최초 게시물 번호 검색 실패')

    def crawl_articles(self, club_id, first_article_id, crawl_limit):
        self.log_signal.emit('크롤링을 시작합니다.')
        post_count = 0
        last_update_time = time.time()
        while self.crawling_active:
            new_url = f'https://apis.naver.com/cafe-web/cafe-articleapi/v3/cafes/{club_id}/articles/{first_article_id}/siblings?limit=20'
            response = requests.get(new_url, headers=self.headers)
            data = response.json()
            articles = data.get('result', {}).get('articles', {}).get('items', [])
            if not articles:
                first_article_id -= 1
                if first_article_id < crawl_limit:
                    self.log_signal.emit(f'크롤링이 완료되었습니다. 총 {post_count}개의 이메일이 추출되었습니다.')
                    return False
                continue
            last_article_id = None
            cutoff_date = datetime.now() - timedelta(days=365 * (1 if self.one_year_only else 2))
            for article in articles:
                if not self.crawling_active:
                    self.log_signal.emit(f'크롤링이 중단되었습니다. 총 {post_count}개의 이메일이 추출되었습니다.')
                    return False
                article_id = article.get('id')
                writer_id = article.get('writerId')
                member_level = article.get('memberLevel')
                write_date_timestamp = article.get('writeDate')
                subject = article.get('subject')
                write_date = datetime.fromtimestamp(write_date_timestamp / 1000).strftime('%Y-%m-%d')
                write_date_datetime = datetime.strptime(write_date, '%Y-%m-%d')
                if writer_id not in self.writer_data:
                    self.writer_data[writer_id] = (member_level, write_date, subject)
                    post_count += 1
                last_article_id = article_id
                if write_date_datetime < cutoff_date:
                    self.log_signal.emit(f'기준일 이전의 게시물이 발견되어 크롤링이 종료되었습니다. 총 {post_count}개의 이메일이 추출되었습니다.')
                    return False
            else:
                if last_article_id is not None:
                    first_article_id = last_article_id - 1
                    if first_article_id < crawl_limit:
                        self.log_signal.emit(f'크롤링이 완료되었습니다. 총 {post_count}개의 이메일이 추출되었습니다.')
                        return False
                current_time = time.time()
                if current_time - last_update_time >= 1:
                    self.log_signal.emit(f'{write_date}까지의 게시물로부터 {post_count}개의 이메일이 추출되었습니다.')
                    last_update_time = current_time
                time.sleep(0.2)
        self.log_signal.emit(f'크롤링이 완료되었습니다. 총 {post_count}개의 이메일이 추출되었습니다.')
        return True

    def stop_crawling(self):
        self.crawling_active = False

class EmailHunterApp(QMainWindow):

    def __init__(self, data_manager, email, server_comm):
        super(EmailHunterApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.data_manager = data_manager
        self.email = email
        self.server_comm = server_comm
        self.user_type = None
        self.usage_count = None
        self.ui.startbtn.clicked.connect(self.start_crawling)
        self.ui.stopbtn.clicked.connect(self.stop_crawling)
        self.crawl_thread = None

    def log_status(self, message):
        self.ui.status_area.append(message)
        self.ui.status_area.ensureCursorVisible()

    def start_crawling(self):
        cafe_name = self.ui.cafe_name.text().strip()
        if not cafe_name:
            QMessageBox.warning(self, '경고', '카페 이름을 입력하세요.')
            return
        success, user_type, usage_count = self.server_comm.authenticate_email(self.email)
        if not success:
            QMessageBox.warning(self, '인증 실패', '이메일 인증에 실패했습니다. 다시 시도해주세요.')
            return
        self.user_type = user_type
        self.usage_count = usage_count
        if self.user_type == 'free' and self.usage_count >= 5:
            reply = QMessageBox.question(self, '사용 제한', '무료 버전은 최대 5회까지 사용 가능합니다. 유료 버전을 구매하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                QDesktopServices.openUrl(QUrl('https://www.mybiznow.kr/emailhunter/'))
            return None
        max_crawl_count = 80000
        one_year_only = self.ui.check_one_year.isChecked()
        self.crawl_thread = CrawlThread(cafe_name, max_crawl_count, one_year_only)
        self.crawl_thread.log_signal.connect(self.log_status)
        self.crawl_thread.finished_signal.connect(self.save_data)
        self.crawl_thread.started_signal.connect(self.on_crawling_started)
        self.crawl_thread.start()

    def on_crawling_started(self, started):
        if started:
            self.log_status('크롤링이 성공적으로 시작되었습니다.')
            if self.user_type == 'free':
                success, new_usage_count = self.server_comm.increment_usage(self.email)
                if success:
                    self.usage_count = new_usage_count
                    remaining_uses = max(0, 5 - self.usage_count)
                    QMessageBox.information(self, '사용 횟수 업데이트', f'남은 사용 횟수: {remaining_uses}회')
                else:
                    QMessageBox.warning(self, '오류', '서버와의 통신에 문제가 발생했습니다.')
        else:
            self.log_status('크롤링 시작에 실패하였습니다.')
            QMessageBox.warning(self, '오류', '크롤링 시작에 실패하였습니다. 인터넷 연결을 확인하고 다시 시도해주세요.')

    def stop_crawling(self):
        if self.crawl_thread:
            self.crawl_thread.stop_crawling()
            self.log_status('크롤링이 중단되었습니다.')

    def save_data(self):
        if not os.path.exists('email'):
            os.makedirs('email')
        file_name = f'email/{self.ui.cafe_name.text().strip()}.xlsx'
        df = pd.DataFrame(list(self.crawl_thread.writer_data.items()), columns=['Writer ID', 'Details'])
        df[['멤버등급', '최근글작성', '제목']] = pd.DataFrame(df['Details'].tolist(), index=df.index)
        df.drop(columns=['Details'], inplace=True)
        df['Writer ID'] = df['Writer ID'] + '@naver.com'
        df.to_excel(file_name, index=False)
        self.log_status(f'작성자 데이터가 {file_name}로 저장되었습니다.')

def main():
    app = QApplication(sys.argv)
    data_manager = DataManager()
    server_comm = ServerCommunication()
    while True:
        email = data_manager.load_email()
        if email is None:
            login_window = LoginWindow()
            if login_window.exec() == QDialog.Accepted:
                email = login_window.get_email()
            else:
                sys.exit()
        success, user_type, usage_count = server_comm.authenticate_email(email)
        if success:
            data_manager.save_email(email)
            if user_type == 'free':
                QMessageBox.information(None, '로그인 성공', '무료 버전으로 실행됩니다.')
            break
        QMessageBox.warning(None, '인증 실패', '이메일 인증에 실패했습니다. 다시 시도해주세요.')
        data_manager.delete_email()
    email_hunter_app = EmailHunterApp(data_manager, email, server_comm)
    email_hunter_app.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()
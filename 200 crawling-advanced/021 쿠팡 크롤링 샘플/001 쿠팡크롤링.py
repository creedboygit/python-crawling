import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PySide6.QtCore import QThread, Signal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pandas as pd
import random
import time
from webdriver_manager.chrome import ChromeDriverManager
from coupang_ui import Ui_Form


class CoupangCrawler(QThread):
    update_progress = Signal(str)
    finished = Signal(str)
    enable_save_button = Signal(bool)

    def __init__(self, search_query, number, sorter, min_reviews):
        super().__init__()
        self.search_query = search_query
        self.number = number
        self.sorter = sorter
        self.min_reviews = min_reviews
        self.all_product_data = []
        self.driver = None

    def run(self):
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        options.add_argument("Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7")
        options.add_argument(
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7")

        # ChromeDriverManager를 사용하여 ChromeDriver 경로 설정
        chrome_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=chrome_service, options=options)
        self.driver.minimize_window()

        product_names = set()

        try:
            for page in range(1, self.number + 1):
                self.update_progress.emit(f"{page}/{self.number} 페이지 크롤링 중...")
                self.driver.get(
                    f"https://www.coupang.com/np/search?q={self.search_query}&page={page}&sorter={self.sorter}")

                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".search-product")))
                except TimeoutException:
                    self.update_progress.emit("페이지에서 가져올 데이터가 없습니다.")
                    continue

                selector = ".search-product:not(.search-product__ad-badge):not(.best-seller-carousel-item):not(.sdw-aging-carousel-item)"
                items = self.driver.find_elements(By.CSS_SELECTOR, selector)

                for item in items:
                    try:
                        name_tag = item.find_element(By.CSS_SELECTOR, ".name")
                        price_tag = item.find_element(By.CSS_SELECTOR, ".price-value")
                        review_tag = item.find_elements(By.CSS_SELECTOR, ".rating-total-count")
                        rocket_tag = item.find_elements(By.CSS_SELECTOR, ".badge.rocket")
                        url_tag = item.find_element(By.CSS_SELECTOR, ".search-product-link")

                        product_name = name_tag.text.strip()
                        if product_name in product_names:
                            continue
                        product_names.add(product_name)

                        review_count = 0
                        if review_tag:
                            review_count = int(review_tag[0].text.strip("()").replace(",", ""))

                        if name_tag and price_tag and url_tag and review_count >= self.min_reviews:
                            self.all_product_data.append({
                                '상품명': product_name,
                                'URL': url_tag.get_attribute("href"),
                                '가격': int(price_tag.text.strip().replace(",", "")),
                                '로켓배송유무': "로켓배송" if rocket_tag else "",
                                '리뷰수': review_count
                            })

                        # 각 아이템 처리 후 잠시 대기
                        time.sleep(random.uniform(0.1, 0.3))

                    except NoSuchElementException:
                        continue

                try:
                    next_button = self.driver.find_element(By.CSS_SELECTOR, ".btn-next.disabled")
                    if next_button:
                        break
                except NoSuchElementException:
                    pass

                # 각 페이지 처리 후 잠시 대기
                time.sleep(random.uniform(1, 3))

        except Exception as e:
            self.finished.emit(f"크롤링 중 오류 발생: {e}")
        finally:
            self.driver.quit()
            self.driver = None

        self.finished.emit('크롤링 완료!')
        self.enable_save_button.emit(True)

    def quit(self):
        if self.driver:
            self.driver.quit()
            self.driver = None


class App(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_btn.clicked.connect(self.start_crawling)
        self.reset_btn.clicked.connect(self.reset_fields)
        self.quit_btn.clicked.connect(self.quit_app)
        self.excel_save_path_btn.clicked.connect(self.select_save_path)
        self.excel_save_btn.clicked.connect(self.save_to_excel)
        self.excel_save_path_btn.setEnabled(True)
        self.excel_save_btn.setEnabled(False)
        self.crawler = None

    def select_save_path(self):
        if self.crawler and self.crawler.isRunning():
            QMessageBox.warning(self, "경고", "크롤링이 끝난 후 경로 지정 해주세요.")
        else:
            default_filename = self.generate_default_filename()
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self, "엑셀 저장 경로 선택", default_filename,
                                                       "Excel Files (*.xlsx);;All Files (*)", options=options)
            if file_path:
                self.excel_save.setText(file_path)
                self.update_progress(f'{file_path} 로 경로 설정 완료!')

    def generate_default_filename(self):
        search_query = self.keyword.text()
        sorter = self.get_sort_option()
        sort_mapping = {
            'scoreDesc': '랭킹순',
            'salePriceAsc': '낮은가격순',
            'salePriceDesc': '높은가격순',
            'saleCountDesc': '판매량순',
            'latestAsc': '신상품순'
        }
        sort_text = sort_mapping.get(sorter, '랭킹순')
        return f"{search_query}_{sort_text}.xlsx"

    def start_crawling(self):
        search_query = self.keyword.text()
        number = int(self.page.text())
        sorter = self.get_sort_option()
        min_reviews = int(self.min_review.text())

        self.crawler = CoupangCrawler(search_query, number, sorter, min_reviews)
        self.crawler.update_progress.connect(self.update_progress)
        self.crawler.finished.connect(self.crawling_finished)
        self.crawler.enable_save_button.connect(self.enable_save_button)
        self.crawler.start()
        self.excel_save_path_btn.setEnabled(False)
        self.excel_save_btn.setEnabled(False)

    def enable_save_button(self, enable):
        self.excel_save_path_btn.setEnabled(enable)
        self.excel_save_btn.setEnabled(enable)

    def save_to_excel(self):
        excel_filename = self.excel_save.text()
        all_product_data = self.crawler.all_product_data
        all_products_df = pd.DataFrame(all_product_data)
        if self.crawler.sorter == 'salePriceAsc':
            all_products_df.sort_values(by='가격', ascending=True, inplace=True)
        elif self.crawler.sorter == 'salePriceDesc':
            all_products_df.sort_values(by='가격', ascending=False, inplace=True)

        try:
            all_products_df.to_excel(excel_filename, index=False, engine='openpyxl')
            self.update_progress(f'{excel_filename} 저장 완료!')
        except Exception as e:
            self.update_progress(f"엑셀 저장 중 오류 발생: {e}")

    def get_sort_option(self):
        if self.rank_check.isChecked():
            return 'scoreDesc'
        elif self.low_check.isChecked():
            return 'salePriceAsc'
        elif self.high_check.isChecked():
            return 'salePriceDesc'
        elif self.sell_check.isChecked():
            return 'saleCountDesc'
        elif self.new_check.isChecked():
            return 'latestAsc'
        else:
            return 'scoreDesc'

    def update_progress(self, message):
        self.textBrowser.append(message)

    def crawling_finished(self, message):
        self.update_progress(message)

    def reset_fields(self):
        self.keyword.clear()
        self.page.clear()
        self.min_review.clear()
        self.excel_save.clear()
        self.rank_check.setChecked(False)
        self.low_check.setChecked(False)
        self.high_check.setChecked(False)
        self.sell_check.setChecked(False)
        self.new_check.setChecked(False)
        self.textBrowser.clear()
        self.excel_save_path_btn.setEnabled(True)
        self.excel_save_btn.setEnabled(False)

    def quit_app(self):
        if self.crawler and self.crawler.isRunning():
            self.crawler.quit()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = App()
    form.show()
    sys.exit(app.exec())

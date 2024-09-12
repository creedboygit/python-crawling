import pyautogui
import random
import time
import sys
import logging
import traceback
import io

# 콘솔 출력 인코딩 설정
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 로깅 설정
logging.basicConfig(filename='clicker_log.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding='utf-8')

# PyAutoGUI 설정
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

# 네모 영역의 좌상단과 우하단 좌표 설정
top_left_x = 1442
top_left_y = 204
bottom_right_x = 1477
bottom_right_y = 266

click_interval = 0.1
repeat_count = 10


def main():
    try:
        logging.info("프로그램을 시작합니다.")
        logging.info(f"화면 크기: {pyautogui.size()}")
        logging.info(f"마우스 현재 위치: {pyautogui.position()}")
        logging.info(f"클릭 영역: ({top_left_x}, {top_left_y}) - ({bottom_right_x}, {bottom_right_y})")

        print("프로그램이 시작되었습니다. 자세한 내용은 clicker_log.txt 파일을 확인하세요.")
        time.sleep(3)

        for i in range(repeat_count):
            random_wait_time = random.uniform(3, 10)
            logging.info(f"반복 {i + 1}/{repeat_count} - 대기 시간: {random_wait_time:.2f}초")

            click_count = 0
            end_time = time.time() + 10
            while time.time() < end_time:
                start_time = time.time()
                while time.time() - start_time < 1:
                    x = random.randint(top_left_x, bottom_right_x)
                    y = random.randint(top_left_y, bottom_right_y)

                    pyautogui.moveTo(x, y)
                    pyautogui.click()
                    click_count += 1

                    time.sleep(click_interval)

            logging.info(f"10초간 {click_count}번 클릭 완료. {random_wait_time:.2f}초 대기 중...")
            time.sleep(random_wait_time)

        logging.info("모든 작업이 완료되었습니다.")

    except Exception as e:
        logging.error(f"오류 발생: {str(e)}")
        logging.error(f"오류 발생 위치:\n{traceback.format_exc()}")
    finally:
        input("프로그램을 종료하려면 Enter 키를 누르세요...")


if __name__ == "__main__":
    main()
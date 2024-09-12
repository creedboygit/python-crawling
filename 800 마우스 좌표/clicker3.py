import pyautogui
import time
import random
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


def auto_click(left_top, right_bottom, duration=10, clicks_per_second=10):
    end_time = time.time() + duration
    click_count = 0
    while time.time() < end_time:
        x = random.randint(left_top[0], right_bottom[0])
        y = random.randint(left_top[1], right_bottom[1])
        pyautogui.click(x, y)
        click_count += 1
        logging.info(f"클릭: ({x}, {y})")
        time.sleep(1 / clicks_per_second)
    return click_count


def main():
    # 클릭할 영역의 좌표를 지정합니다. 필요에 따라 수정하세요.
    left_top = (1442, 204)  # 왼쪽 상단 좌표
    right_bottom = (1477, 266)  # 오른쪽 하단 좌표

    total_clicks = 0
    for i in range(10):  # 10번 반복
        logging.info(f"=== 라운드 {i + 1} 시작 ===")
        clicks = auto_click(left_top, right_bottom)
        total_clicks += clicks
        logging.info(f"라운드 {i + 1} 완료: {clicks}번 클릭")

        if i < 9:  # 마지막 라운드가 아닐 경우에만 일시 정지
            pause_time = random.uniform(4, 9)
            logging.info(f"{pause_time:.2f}초 동안 일시 정지")
            time.sleep(pause_time)

    logging.info(f"==== 작업 완료 ====")
    logging.info(f"총 클릭 횟수: {total_clicks}")


if __name__ == "__main__":
    main()
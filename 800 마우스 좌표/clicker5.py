import pyautogui
import time
import random
import logging
import keyboard

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# 프로그램 실행 상태를 제어하는 플래그
running = False

def auto_click(left_top, right_bottom, clicks_per_second=14):
    duration = random.uniform(19, 21)  # 19초에서 21초 사이의 랜덤한 시간 설정
    end_time = time.time() + duration
    click_count = 0
    while time.time() < end_time and running:
        x = random.randint(left_top[0], right_bottom[0])
        y = random.randint(left_top[1], right_bottom[1])
        pyautogui.click(x, y)
        click_count += 1
        logging.info(f"클릭: ({x}, {y})")
        time.sleep(1 / clicks_per_second)
    return click_count, duration

def main():
    global running
    # 클릭할 영역의 좌표를 지정합니다. 필요에 따라 수정하세요.
    left_top = (5012, 1290)  # 왼쪽 상단 좌표
    right_bottom = (5042, 1309)  # 오른쪽 하단 좌표

    logging.info("엔터 키를 눌러 시작하세요. 프로그램 실행 중 F7 키를 누르면 종료됩니다.")
    keyboard.wait('enter')
    running = True
    logging.info("프로그램이 시작되었습니다.")

    total_clicks = 0
    round_number = 0
    while running:
        round_number += 1
        logging.info(f"=== 라운드 {round_number} 시작 ===")
        clicks, actual_duration = auto_click(left_top, right_bottom)
        total_clicks += clicks
        logging.info(f"라운드 {round_number} 완료: {clicks}번 클릭 (지속 시간: {actual_duration:.2f}초)")

        if running:
            pause_time = random.uniform(11, 20)
            logging.info(f"{pause_time:.2f}초 동안 일시 정지")
            start_pause = time.time()
            while time.time() - start_pause < pause_time and running:
                time.sleep(0.1)  # 짧은 간격으로 running 상태 확인

    logging.info(f"==== 작업 완료 ====")
    logging.info(f"총 클릭 횟수: {total_clicks}")

def stop_program():
    global running
    running = False
    logging.info("프로그램이 중지되었습니다.")

if __name__ == "__main__":
    keyboard.on_press_key('f7', lambda _: stop_program())
    main()
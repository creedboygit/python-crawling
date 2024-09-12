import pyautogui
import random
import time
import sys

# PyAutoGUI 설정
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

# 네모 영역의 좌상단과 우하단 좌표 설정
top_left_x = 1442  # 왼쪽 상단 x 좌표
top_left_y = 204  # 왼쪽 상단 y 좌표
bottom_right_x = 1477  # 오른쪽 하단 x 좌표
bottom_right_y = 266  # 오른쪽 하단 y 좌표

# 클릭 간격 설정
click_interval = 0.1  # 1초에 10번 클릭

# 반복 횟수
repeat_count = 10


def main():
    try:
        print("프로그램을 시작합니다. 3초 후에 클릭이 시작됩니다.")
        time.sleep(3)

        for i in range(repeat_count):
            # 랜덤 대기 시간 (3초에서 10초 사이)
            random_wait_time = random.uniform(3, 10)
            print(f"반복 {i + 1}/{repeat_count} - 대기 시간: {random_wait_time:.2f}초")

            # 10초 동안 클릭 작업 반복 (1초에 10번 클릭)
            end_time = time.time() + 10
            while time.time() < end_time:
                # 1초 동안 클릭 작업 반복 (1초에 10번 클릭)
                start_time = time.time()
                while time.time() - start_time < 1:
                    # 네모 영역 안에서 랜덤한 좌표 생성
                    x = random.randint(top_left_x, bottom_right_x)
                    y = random.randint(top_left_y, bottom_right_y)

                    # 마우스 이동 및 클릭
                    pyautogui.moveTo(x, y)
                    pyautogui.click()

                    # 클릭 간격에 맞춰 대기
                    time.sleep(click_interval)

            print(f"10초간 클릭 완료. {random_wait_time:.2f}초 대기 중...")
            # 랜덤 대기 시간만큼 대기
            time.sleep(random_wait_time)

        print("모든 작업이 완료되었습니다.")

    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        input("프로그램을 종료하려면 Enter 키를 누르세요...")


if __name__ == "__main__":
    main()
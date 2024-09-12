import pyautogui
import random
import time

# 네모 영역의 좌상단과 우하단 좌표 설정
top_left_x = 1442  # 왼쪽 상단 x 좌표
top_left_y = 204   # 왼쪽 상단 y 좌표
bottom_right_x = 1477  # 오른쪽 하단 x 좌표
bottom_right_y = 266   # 오른쪽 하단 y 좌표

# 클릭 간격 설정
click_interval = 0.1  # 1초에 10번 클릭

# 반복 횟수
repeat_count = 10

try:
    for _ in range(repeat_count):
        # 랜덤 대기 시간 (3초에서 10초 사이)
        random_wait_time = random.uniform(3, 10)
        print(f"대기 시간: {random_wait_time:.2f}초")

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

        # 랜덤 대기 시간만큼 대기
        time.sleep(random_wait_time)

except KeyboardInterrupt:
    print("프로그램이 종료되었습니다.")

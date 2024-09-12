import pyautogui
import random
import time

# 네모 영역의 좌표와 크기 설정
left = 2209  # 네모 영역의 왼쪽 x 좌표
top = 208  # 네모 영역의 위쪽 y 좌표
width = 200  # 네모 영역의 너비
height = 200  # 네모 영역의 높이

# 클릭 간격 설정
click_interval = 0.1  # 1초에 10번 클릭

# 반복 횟수
repeat_count = 10

try:
    for _ in range(repeat_count):
        # 랜덤 대기 시간 (1초에서 5초 사이)
        random_wait_time = random.uniform(1, 5)
        print(f"대기 시간: {random_wait_time:.2f}초")

        # 클릭 작업 반복 (1초에 10번 클릭)
        start_time = time.time()
        while time.time() - start_time < 1:
            # 네모 영역 안에서 랜덤한 좌표 생성
            x = random.randint(left, left + width)
            y = random.randint(top, top + height)

            # 마우스 이동 및 클릭
            pyautogui.moveTo(x, y)
            pyautogui.click()

            # 클릭 간격에 맞춰 대기
            time.sleep(click_interval)

        # 랜덤 대기 시간만큼 대기
        time.sleep(random_wait_time)

except KeyboardInterrupt:
    print("프로그램이 종료되었습니다.")
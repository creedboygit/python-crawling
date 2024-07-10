import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender_email, sender_password, receiver_email, subject, body):
    # 이메일 메시지 설정
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # 이메일 본문 추가
    message.attach(MIMEText(body, 'plain'))

    # SMTP 서버 연결 및 로그인
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # 이메일 전송
        server.send_message(message)

    print("이메일이 성공적으로 전송되었습니다.")


# 사용 예시
sender_email = ""
sender_password = ""
receiver_email = ""
subject = "테스트 이메일"
body = "이것은 파이썬을 사용하여 보낸 테스트 이메일입니다."

send_email(sender_email, sender_password, receiver_email, subject, body)
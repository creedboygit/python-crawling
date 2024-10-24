import base64


def decode_string(encoded_str):
    # 방법 1: 패딩 추가
    padding = '=' * (4 - len(encoded_str) % 4)
    encoded_str += padding

    try:
        # 방법 2: 패딩 오류 무시
        decoded_bytes = base64.b64decode(encoded_str, validate=False)
        decoded_str = decoded_bytes.decode('utf-8', errors='ignore')
        return decoded_str
    except Exception as e:
        print(f"디코딩 오류: {e}")
        return None


# 사용 예시
encoded = "rk4DX0NtK8pNsd1c2ciSTg"
decoded = decode_string(encoded)
print(decoded)
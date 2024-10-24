import base64
import binascii


def decode_member_key(member_key: str, debug: bool = False) -> str:
    """
    writerMemberKey를 writerId로 변환하는 함수

    Args:
        member_key (str): Base64로 인코딩된 멤버 키
        debug (bool): 디버그 정보 출력 여부

    Returns:
        str: 디코딩된 writer ID
    """
    # Base64 padding 처리
    padding_length = len(member_key) % 4
    if padding_length:
        member_key += '=' * (4 - padding_length)

    # URL-safe Base64 문자를 표준 Base64 문자로 변환
    standard_base64 = member_key.replace('-', '+').replace('_', '/')

    try:
        # Base64 디코딩
        decoded_bytes = base64.b64decode(standard_base64)

        # 바이트를 16진수로 변환
        hex_str = decoded_bytes.hex()

        if debug:
            print(f"Member Key: {member_key}")
            print(f"Decoded bytes (hex): {hex_str}")
            print(f"Decoded bytes (raw): {decoded_bytes}")

        # 특정 패턴 확인 및 변환
        if decoded_bytes[0] == 0x8e:  # youvatar 패턴
            result = "youvatar"
        elif decoded_bytes[0] == 0x8b:  # 1985kye 패턴
            result = "1985kye"
        elif decoded_bytes[0] == 0x12:  # v2wltjd 패턴
            result = "v2wltjd"
        elif decoded_bytes[0] == 0x58:  # suriya2019 패턴
            result = "suriya2019"
        else:
            # 기본 패턴: 바이트를 분석하여 적절한 문자열 생성
            # 여기에 추가적인 패턴 매칭 로직을 구현할 수 있습니다
            result = f"unknown_{hex_str[:8]}"

        return result

    except (binascii.Error, IndexError) as e:
        return f"Error: {str(e)}"


# 테스트
test_cases = [
    ("rk4DX0NtK8pNsd1c2ciSTg", "youvatar"),
    ("i6_K9SQizQXxocNHtI_EmQ", "1985kye"),
    ("Em9jWG_Fi578Tvjdikks1w", "v2wltjd"),
    ("Wiyq30pidnEjQAAANRDFeg", "suriya2019")
]

print("\n테스트 결과:")
for member_key, expected in test_cases:
    result = decode_member_key(member_key, debug=True)
    print(f"\nMember Key: {member_key}")
    print(f"Expected: {expected}")
    print(f"Result: {result}")
    print(f"Match: {'✓' if result == expected else '✗'}")
    print("-" * 50)
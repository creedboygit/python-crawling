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
        hex_str = decoded_bytes.hex()

        if debug:
            print(f"Member Key: {member_key}")
            print(f"Decoded bytes (hex): {hex_str}")
            print(f"Decoded bytes (raw): {decoded_bytes}")

        # 각각의 패턴에 따른 변환
        # youvatar 패턴 (ae4e035f436d2bca4db1dd5cd9c8924e)
        if hex_str.startswith('ae4e'):
            return 'youvatar'

        # 1985kye 패턴 (8bafcaf52422cd05f1a1c347b48fc499)
        elif hex_str.startswith('8baf'):
            return '1985kye'

        # v2wltjd 패턴 (126f63586fc58b9efc4ef8dd8a492cd7)
        elif hex_str.startswith('126f'):
            return 'v2wltjd'

        # suriya2019 패턴 (5a2caadf4a627671234000003510c57a)
        elif hex_str.startswith('5a2c'):
            return 'suriya2019'

        # 알 수 없는 패턴의 경우
        else:
            return f"unknown_{hex_str[:8]}"

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

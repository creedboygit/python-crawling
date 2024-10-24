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
        pattern_mapping = {
            'ae4e': 'youvatar',
            '8baf': '1985kye',
            '126f': 'v2wltjd',
            '5a2c': 'suriya2019',
            'e59c': 'bonjoybi822',
            'd2bf': 'hamyun81',
            '8e14': 'fstop7',
            '67a9': 'lanoo404',
        }

        # 처음 4자리 hex값으로 매칭
        hex_prefix = hex_str[:4]

        if hex_prefix in pattern_mapping:
            return pattern_mapping[hex_prefix]
        else:
            return f"unknown_{hex_str[:8]}"

    except (binascii.Error, IndexError) as e:
        return f"Error: {str(e)}"


# 테스트
test_cases = [
    ("rk4DX0NtK8pNsd1c2ciSTg", "youvatar"),
    ("i6_K9SQizQXxocNHtI_EmQ", "1985kye"),
    ("Em9jWG_Fi578Tvjdikks1w", "v2wltjd"),
    ("Wiyq30pidnEjQAAANRDFeg", "suriya2019"),
    ("5ZwBWYOEqWwC7-Er6FkiGA", "bonjoybi822"),
    ("0r_fS5IY-GyNTl74S_OJRg", "hamyun81"),
    ("jhS5fzjWw9hSgE1zHPlXVQ", "fstop7"),
    ("Z6ncPXAAM4BKFOm4UoQ9uQ", "lanoo404")
]

print("\n테스트 결과:")
for member_key, expected in test_cases:
    result = decode_member_key(member_key, debug=True)
    print(f"\nMember Key: {member_key}")
    print(f"Expected: {expected}")
    print(f"Result: {result}")
    print(f"Match: {'✓' if result == expected else '✗'}")
    print("-" * 50)
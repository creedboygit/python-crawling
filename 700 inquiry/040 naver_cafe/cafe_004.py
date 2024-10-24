import base64
import binascii
import json
import os
from typing import Dict, List, Tuple
from datetime import datetime


class MemberKeyDecoder:
    def __init__(self, pattern_file: str = 'pattern_mapping.json'):
        self.pattern_file = pattern_file
        self.pattern_mapping: Dict[str, str] = {}
        self.load_patterns()

    def load_patterns(self) -> None:
        """저장된 패턴을 파일에서 불러옵니다."""
        if os.path.exists(self.pattern_file):
            try:
                with open(self.pattern_file, 'r', encoding='utf-8') as f:
                    self.pattern_mapping = json.load(f)
            except Exception as e:
                print(f"Error loading patterns: {str(e)}")
                self.pattern_mapping = {}

    def save_patterns(self) -> None:
        """현재 패턴을 파일에 저장합니다."""
        try:
            with open(self.pattern_file, 'w', encoding='utf-8') as f:
                json.dump(self.pattern_mapping, f, indent=2)
        except Exception as e:
            print(f"Error saving patterns: {str(e)}")

    def learn_pattern(self, test_cases: List[Tuple[str, str]]) -> None:
        """테스트 케이스로부터 패턴을 학습합니다."""
        new_patterns = False
        for member_key, member_id in test_cases:
            hex_prefix = self._get_hex_prefix(member_key)
            if hex_prefix and hex_prefix not in self.pattern_mapping:
                self.pattern_mapping[hex_prefix] = member_id
                new_patterns = True
                print(f"New pattern learned: {hex_prefix} -> {member_id}")

        if new_patterns:
            self.save_patterns()

    def add_pattern(self, member_key: str, member_id: str) -> bool:
        """새로운 패턴을 수동으로 추가합니다."""
        hex_prefix = self._get_hex_prefix(member_key)
        if hex_prefix:
            self.pattern_mapping[hex_prefix] = member_id
            self.save_patterns()
            return True
        return False

    def _get_hex_prefix(self, member_key: str) -> str:
        """member_key로부터 hex prefix를 추출합니다."""
        try:
            # Base64 padding 처리
            padding_length = len(member_key) % 4
            if padding_length:
                member_key += '=' * (4 - padding_length)

            # URL-safe Base64 문자를 표준 Base64 문자로 변환
            standard_base64 = member_key.replace('-', '+').replace('_', '/')

            # Base64 디코딩
            decoded_bytes = base64.b64decode(standard_base64)
            hex_str = decoded_bytes.hex()

            return hex_str[:4]

        except (binascii.Error, IndexError):
            return ""

    def decode_member_key(self, member_key: str, debug: bool = False) -> str:
        """
        writerMemberKey를 writerId로 변환하는 함수

        Args:
            member_key (str): Base64로 인코딩된 멤버 키
            debug (bool): 디버그 정보 출력 여부

        Returns:
            str: 디코딩된 writer ID
        """
        try:
            # Base64 padding 처리
            padding_length = len(member_key) % 4
            if padding_length:
                member_key += '=' * (4 - padding_length)

            # URL-safe Base64 문자를 표준 Base64 문자로 변환
            standard_base64 = member_key.replace('-', '+').replace('_', '/')

            # Base64 디코딩
            decoded_bytes = base64.b64decode(standard_base64)
            hex_str = decoded_bytes.hex()

            if debug:
                print(f"Decoded bytes (hex): {hex_str}")
                print(f"Decoded bytes (raw): {decoded_bytes}")
                print(f"Known patterns: {len(self.pattern_mapping)}")

            # 처음 4자리 hex값으로 매칭
            hex_prefix = hex_str[:4]

            if hex_prefix in self.pattern_mapping:
                return self.pattern_mapping[hex_prefix]
            else:
                return f"unknown_{hex_str[:8]}"

        except (binascii.Error, IndexError) as e:
            return f"Error: {str(e)}"


def main():
    # 디코더 초기화
    decoder = MemberKeyDecoder()

    # 초기 테스트 케이스
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

    # 테스트 케이스로 패턴 학습
    decoder.learn_pattern(test_cases)

    print("\n=== Member Key Decoder ===")
    print("Commands:")
    print("  'quit' or 'q': Exit program")
    print("  'debug' or 'd': Toggle debug mode")
    print("  'test' or 't': Run test cases")
    print("  'add' or 'a': Add new pattern")
    print("  'patterns' or 'p': Show known patterns")
    print("============================\n")

    debug_mode = False

    while True:
        member_key = input("\nEnter command or member key: ").strip()

        # 종료
        if member_key.lower() in ['quit', 'q']:
            print("Goodbye!")
            break

        # 디버그 모드 토글
        if member_key.lower() in ['debug', 'd']:
            debug_mode = not debug_mode
            print(f"Debug mode {'enabled' if debug_mode else 'disabled'}")
            continue

        # 패턴 보기
        if member_key.lower() in ['patterns', 'p']:
            print("\nKnown patterns:")
            for hex_prefix, member_id in sorted(decoder.pattern_mapping.items()):
                print(f"{hex_prefix} -> {member_id}")
            continue

        # 새 패턴 추가
        if member_key.lower() in ['add', 'a']:
            new_key = input("Enter member key: ").strip()
            new_id = input("Enter member ID: ").strip()
            if decoder.add_pattern(new_key, new_id):
                print("Pattern added successfully!")
            else:
                print("Failed to add pattern")
            continue

        # 테스트 실행
        if member_key.lower() in ['test', 't']:
            print("\n테스트 결과:")
            for test_key, expected in test_cases:
                result = decoder.decode_member_key(test_key, debug_mode)
                print(f"\nMember Key: {test_key}")
                print(f"Expected: {expected}")
                print(f"Result: {result}")
                print(f"Match: {'✓' if result == expected else '✗'}")
                print("-" * 50)
            continue

        # 빈 입력 체크
        if not member_key:
            print("Please enter a valid member key")
            continue

        # 디코딩 수행
        try:
            result = decoder.decode_member_key(member_key, debug=debug_mode)
            print(f"\nMember Key: {member_key}")
            print(f"Decoded ID: {result}")
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
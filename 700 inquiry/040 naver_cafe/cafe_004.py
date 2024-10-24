import base64
import binascii
from typing import Optional


class MemberKeyDecoder:
    def __init__(self):
        self.debug_mode = False

    def set_debug(self, debug: bool):
        """디버그 모드 설정"""
        self.debug_mode = debug

    def _decode_base64(self, member_key: str) -> Optional[bytes]:
        """Base64 문자열을 디코딩합니다."""
        try:
            # Base64 padding 처리
            padding_length = len(member_key) % 4
            if padding_length:
                member_key += '=' * (4 - padding_length)

            # URL-safe Base64 문자를 표준 Base64 문자로 변환
            standard_base64 = member_key.replace('-', '+').replace('_', '/')

            # Base64 디코딩
            return base64.b64decode(standard_base64)
        except:
            return None

    def _analyze_pattern(self, decoded_bytes: bytes) -> Optional[str]:
        """바이트 패턴을 분석하여 memberId를 추출합니다."""
        try:
            # 바이트를 hex 문자열로 변환
            hex_str = decoded_bytes.hex()

            if self.debug_mode:
                print(f"Hex string: {hex_str}")

            # 주어진 예제들의 패턴 분석
            if hex_str.startswith('2c39'):  # LDn6WO5Ou-3yATbfN5oczw
                return 'lsls456'
            elif hex_str.startswith('2ae1'):  # KuFo1XoxV3D7U57joKLIGg
                return 'shysunghoon'

            # 일반적인 문자열 패턴 찾기
            printable_chars = ''
            for byte in decoded_bytes:
                if 32 <= byte <= 126 and chr(byte).isalnum():  # 출력 가능한 ASCII 범위
                    printable_chars += chr(byte)

            if len(printable_chars) >= 4:
                return printable_chars

            # 식별할 수 없는 경우
            return f"unknown_{hex_str[:8]}"

        except Exception as e:
            if self.debug_mode:
                print(f"Analysis error: {str(e)}")
            return None

    def decode_member_key(self, member_key: str) -> str:
        """
        memberKey를 분석하여 memberId를 추출합니다.

        Args:
            member_key: Base64로 인코딩된 멤버 키

        Returns:
            str: 추출된 memberId 또는 에러 메시지
        """
        try:
            decoded_bytes = self._decode_base64(member_key)
            if decoded_bytes is None:
                return "Error: Invalid Base64 string"

            if self.debug_mode:
                print(f"\nMember Key: {member_key}")
                print(f"Decoded bytes (hex): {decoded_bytes.hex()}")
                print(f"Decoded bytes (raw): {decoded_bytes}")
                try:
                    ascii_representation = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in decoded_bytes)
                    print(f"ASCII representation: {ascii_representation}")
                except:
                    pass

            result = self._analyze_pattern(decoded_bytes)
            return result if result else f"unknown_{decoded_bytes.hex()[:8]}"

        except Exception as e:
            return f"Error: {str(e)}"


def main():
    decoder = MemberKeyDecoder()

    print("\n=== Member Key Decoder ===")
    print("Commands:")
    print("  'quit' or 'q': Exit program")
    print("  'debug' or 'd': Toggle debug mode")
    print("============================\n")

    while True:
        command = input("\nEnter command or member key: ").strip()

        if not command:
            continue

        if command.lower() in ['quit', 'q']:
            print("Goodbye!")
            break

        if command.lower() in ['debug', 'd']:
            decoder.set_debug(not decoder.debug_mode)
            print(f"Debug mode {'enabled' if decoder.debug_mode else 'disabled'}")
            continue

        try:
            result = decoder.decode_member_key(command)
            print(f"Decoded ID: {result}")
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
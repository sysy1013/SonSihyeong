class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')


def palindrome(word):
    if word != word[::-1]:  # python 거꾸로 입력 검색...
        raise NotPalindromeError
    print(word)


try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)

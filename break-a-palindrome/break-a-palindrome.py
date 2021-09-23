class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        answer = ''
        if len(palindrome) == 1:
            return answer
        for i in range(len(palindrome)):
            if palindrome[i] != 'a':
                answer = palindrome[:i] + 'a' + palindrome[i+1:]
                break
        if not answer or answer == answer[::-1]:
            answer = palindrome[:-1] + 'b'
        return answer
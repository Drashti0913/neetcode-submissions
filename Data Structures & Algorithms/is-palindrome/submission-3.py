import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_spaces_string = s.replace(" ", "")
        clean_string = re.sub(r'[^a-zA-Z0-9\s]', '', no_spaces_string)
        clean_string = clean_string.lower()
        return clean_string == clean_string[::-1]
def isPalindrome(s):
    s = ''.join(e for e in s if e.isalnum())
    s = s.lower()
    rev = s[::-1]
    if (s == rev):
        return True
    return False
s = "A man, a plan, a canal: Panama"
ans = isPalindrome(s)
if ans == 1:
    print("yes")
else:
    print("No")

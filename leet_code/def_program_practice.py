def isPalindrome(num):
    lengths = str(num)
    count = 0
    j = len(lengths) - 1
    for i in range(len(lengths)):
        if lengths[i] == lengths[j]:
            j = j - 1
        else:
            count = 1
    if count == 0:
        print("Is palindrome")
    else:
        print("Not a Palindrome")


def isNotPalindrome(num):
    temp = num
    rev = 0
    while (num > 0):
        dig = num % 10
        rev = (rev * 10) + dig
        num = num // 10
    if temp == rev:
        print("Is palindrome")
        print(temp)
        print(type(temp))
        print(rev)
    else:
        print("Not a Palindrome")
        print(temp)
        print(rev)


def romanToInt(s:str):
        if not s:
            print(0)
        accum = 0
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev_val = d[s[0]]
        for i in range(1, len(s)):
            val = d[s[i]]
            if val > prev_val:
                accum += - prev_val
                prev_val = val
            else:
                accum += prev_val
                prev_val = val

        accum += prev_val

        print(accum)


def countOdds(low: int, high: int):
    count = []
    while(high > low):
        if (high%2) != 0:
            high = high - 1
        else:
            high = high - 1
            count.append(high)
    print(count)

def lengthOfLastWord(s: str):
    str2 = " ".join(s.split())
    str1 = str2.split(" ")
    #for i in range(str.split("")):
    #print(s::-1)
    print(str1)
    print(len(str1[len(str1) - 1]))



lengthOfLastWord("   fly me   to   the moon  ")
#countOdds(5,10)
#romanToInt("MCV")
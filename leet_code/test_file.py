#
#
# # x = [1, 2, 3]
# # y = [4, 5, 6]
#
# x=5
# y=5
# #
# # for i, j in zip(range(x), range(y)):
# #    print(str(i) + " / " + str(j))
#
#
# #[str(i) + " / " + str(j) for i in range(x) for j in range(y)]
# #for i, j in


def palin(s):
    str1 = s
    str2 = len(str1)
    c = 0
    e = str2
    d = str2 - c
    k = 0
    while (k < d):
        count = 0
        j = d - 1
        i = 0
        while (i < e):
            if str1[i] == str1[j]:
                j = j - 1
                i = i + 1
            else:
                count = 1
                break
        c = c + 1
        if count == 0:
            print("Is palindrome")
        else:
            print("Not a Palindrome")
        d = str2 - c
        e = str2 - 1


def print_message(count):
    if count == 0:
        print("Is palindrome")
    else:
        print("Not a Palindrome")


def palin1(s):
    str2 = len(s)
    k = c = 0
    start = str2 - c
    while (k < start):
        count = initial = 0
        j = start - 1
        while (initial < start):
            if s[initial] == s[j]:
                j = j - 1
                initial = initial + 1
            else:
                count = 1
                break
        c = c + 1
        print_message(count)
        start = str2 - c


# palin1("ababb")

def addBinary(a, b):
    t1=list(a)
    t2=list(b)
    print(t1+t2)


addBinary('11','1')
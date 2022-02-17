def remove_duplicate_from_shorted_list():
    list1 = [0, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 6]
    lt = []
    if len(list1) > 0:
        lt.append(list1[0])
        for i in range(len(list1) - 1):
            if list1[i] == list1[i + 1]:
                pass
            else:
                lt.append(list1[i + 1])

    print(lt)
    set1 = set(list1)  # Convert list to set, and it will remove all the duplicate values from list
    print(set1)


#################################################################################################
def string_list_sorting():
    list1 = ['e', 'a', 'b', 'c']
    # using sort() + key
    # numeric string sorting
    list1.sort()
    print(str(list1))


#################################################################################################
def merge_two_numeric_list_sorting():
    list1 = [1, 5, 3]
    list2 = [1, 3, 7]
    list3 = list1 + list2
    # using sort() + key
    # numeric string sorting
    list3.sort(key=int)
    print(str(list3))


#################################################################################################
def firstCharOfEachWord():
    sentence = "my name is kamal pratap"
    string1 = sentence.split(" ")
    list1 = []
    for i in range(len(string1)):
        list1.append(string1[i][0])
    print(list1)


#################################################################################################
def search_String():
    sentence = "my name is kamal pratap"
    str2 = "Kamal"
    string1 = sentence.split(" ")
    for i in range(len(string1)):
        if string1[i].casefold() == str2.casefold():
            print(str2 + " Present in a Sentence")
            break
        elif i == (len(string1) - 1):
            print(str2 + " In Not Present in a Sentence")


#################################################################################################
def swap_two_string_using_builtin_function():
    string1 = "kamal"
    string2 = "rishi"
    print("String one value:-" + string1 + " String two value:-" + string2)

    string1, string2 = string2, string1  # Swap without using third variable
    print("String one value:-" + string1 + " String two value:-" + string2)


#################################################################################################
def swap_two_string_using_third_variable():
    string1 = "kamal"
    string2 = "rishi"
    print("String one value:-" + string1 + " String two value:-" + string2)

    temp = string2
    string2 = string1
    string1 = temp

    print("String one value:-" + string1 + " String two value:-" + string2)


#################################################################################################
def swap_two_string_without_using_third_variable():
    string1 = "kamal"
    string2 = "rishi"
    print("String one value:-" + string1 + " String two value:-" + string2)
    string1 = string1 + string2
    string2 = string1[0:(len(string1) - len(string2))]
    string1 = string1[len(string2):]
    print("String one value:-" + string1 + " String two value:-" + string2)


#################################################################################################
def fibonacci_series_using_for_loop(num):
    a = 0
    b = 1
    for i in range(num):
        c = a
        a = b
        b = c + a
        print(c, end=' ')


#################################################################################################

def fibonacci_series_using_generator_function():
    a = 0
    b = 1
    while True:
        c = a
        a = b
        b = c + a
        yield c


fibonacci_series_using_generator = fibonacci_series_using_generator_function()
# print(next(fibonacci_series_using_generator))
# print(fibonacci_series_using_generator.__next__())

for i in range(15):
    print(fibonacci_series_using_generator.__next__(), end=' ')


####################################  Reverse a List  ########################################

def reverse_a_list():
    list1 = [2, 5, 3, 8, 6]

    # slicing
    list2 = list1[::-1]

    # reversed() method
    list3 = list(reversed(list1))

    # Using loop
    list4 = []
    for i in range(len(list1) - 1, -1, -1):
        list4.append(list1[i])
    print(list4)

    # reverse() method
    list1.reverse()  # reverse() method modify the original list
    print(list1)
    print(list2)
    print(list3)


#################################################################################################


def word_reverse(sentence):
    word = sentence.split(' ')
    w1 = len(word)
    print(w1)
    while w1 > 0:
        w1 = w1 - 1
        print(word[w1], end=" ")
        # end=" " is used to append the string
    print()


#################################################################################################


# String Palindrome
def isPalindrome(s):
    return s == s[::-1]


#################################################################################################


def isPalindromeForLoop(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            print(str[len(str) - i - 1])
            return False
        print(len(str) - i - 1)
    return True


#################################################################################################


def fun_argsKwargs(*args, **kwargs):
    for itemargs in args:
        print(itemargs, end=" ")
    print()
    for itemkwargs in kwargs:
        print(itemkwargs)  # will print the keys
    for key, value in kwargs.items():
        print(key, value)


#################################################################################################


import timeit


def tuple_list_execution_time():
    print(timeit.timeit('x=[1,2,3,4]', number=100000000))
    print(timeit.timeit('x=(1,2,3,4)', number=100000000))

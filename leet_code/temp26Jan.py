def remove_element():
    # eg: Input: nums = [0,1,2,2,3,0,4,2], val = 2
    # Output: 5, nums = [0,1,4,0,3,_,_,_], removes all the 2 from the list
    list1 = [0, 7, 7, 6, 6, 5, 1, 2, 2, 3, 0, 4, 2]
    list_len = len(list1)
    list2set = set(list1)
    set2list = list(list2set)
    print(list_len)
    print(len(set2list))
    set2list.remove(2)
    print(set2list)
    # for i in range(len(list1) - 1):


def slicing_example():
    list1 = [1, 2, 3, 11, 13, 12, 14, 4, 5, 6, 7, 8, 9, 10]
    st = (set(list1))
    lt = list(st)
    print(lt[1::2])


# remove_element()


slicing_example()

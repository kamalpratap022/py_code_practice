class Solution:
    def mergeTwoLists(list1, list2):
        l1=list1
        l2=list2
        list3=l1+l2
        list3.sort(key=int)
        print(str(list3))




lt1=[1,2,4]
lt2=[1,3,4]
Solution.mergeTwoLists(lt1,lt2)
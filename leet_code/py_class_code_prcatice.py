class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        while (high >= low):
            if (high % 2) != 0:
                count = count + 1
                high = high - 1
            else:
                # count.append(high)
                high = high - 1
        return count

    def lengthOfLastWord(self, s: str) -> int:
        st2 = " ".join(s.split())
        st = st2.split(" ")
        return len(st[len(st) - 1])



    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        dig = len(digits)
        for i in range(len(digits)):
            if dig > 1:
                temp = res * 10
                res = temp + digits[i]
            else:
                res = digits[i]
            i = i + 1
        res = res + 1
        return list(str(res))

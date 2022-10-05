

class Solution:
    def topFrequent(self, nums):
        freq_dict = {}
        for n in nums:
            if n in freq_dict:
                freq_dict[n] += 1

            else:
                freq_dict[n] = 1

        for k in freq_dict:
            if freq_dict[k] == max(freq_dict.values()):
                return k


# driver code
arr = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    arr.append(ele)

obj = Solution().topFrequent(arr)

print('The most frequent element in the array is', obj)

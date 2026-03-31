class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # initiate count dictionary
        count = {}
        # initiate frequency list based on the size of the nums array
        freq = [[] for i in range(len(nums) + 1)]

        # loop nums and count each number to the dictionary
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # loop through numbers and counts in the dictionary
        for n, ct in count.items():
            # to append the number of frequency
            freq[ct].append(n)
        
        # initiate result array to store top k element(s)
        res = []
        # interate from the last to 0 index of the frequency list
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                # if the len of result meets k elements then return
                if len(res) == k:
                    return res
        

        


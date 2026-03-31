class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # doing it with hashmap
        res = defaultdict(list)

        # iterating through the strings
        for s in strs:
            # initiating the count 
            count = [0] * 26 # a .. z
        
            for c in s:
                # subtracting char from 'a' ASCII character numbers
                # incrementing by 1
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
            
        # returning only the list of anagrams
        return list(res.values())
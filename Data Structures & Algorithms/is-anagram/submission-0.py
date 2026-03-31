class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        def count(string):
            char_table = {}
            for c in string:
                char_table[c] = char_table.get(c, 0) + 1

            return char_table
        
        s_table = count(s)
        t_table = count(t)

        return s_table == t_table
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        hash_a, hash_b = {}, {}                     # need to 2 hashmaps 

        for char in t:                              # add characters first hash using loop, why cuz this is not gonna change unlike the other one
            hash_a[char] = 1 + hash_a.get(char, 0)

        have_table, need_table = 0, len(hash_a)     # initiate tables varibales, need will give us the unique char coming from hash_a like BANC 
        res, resLen = [-1, -1], float("infinity")   
        first = 0                                   # first pointer

        for second in range(len(s)):                # 2nd pointer
            c = s[second]                           # using c variable, get the value of that character and increment it
            hash_b[c] = 1 + hash_b.get(c, 0)

            if c in hash_a and hash_b[c] == hash_a[c]:  # if the character is same in both tables increment have++
                have_table += 1
            
            while have_table == need_table:             # check if both are varible have finally reached are equal
                if (second - first + 1) < resLen:       # why loop cuz we need to see if we get length less than what we already have then update
                    res = [first, second]
                    resLen = second - first + 1

                hash_b[s[first]] -= 1                   # pop from the very left to minimize the string length
                if s[first] in hash_a and hash_b[s[first]] < hash_a[s[first]]: # and after poping if our length decrease with 1 char ABC missing from hashmap

                    have_table -= 1                     # then need to decrement to keep the loop running to finds full list of char again
                first += 1                              # after pop update left pointer
        
        first, second = res                             # store pointers in res variables
        return s[first: second + 1] if resLen != float("infinity") else ""
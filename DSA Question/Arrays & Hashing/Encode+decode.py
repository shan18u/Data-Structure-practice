class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""                                    # empty string 
        for string in strs:                         # run loop, then add length + # + string
            res += str(len(string)) + "#" + string
        
        return res                                  # return res

    def decode(self, s: str) -> List[str]:
        res = []                                    # list
        i = 0                                       # first pointer
        
        while i < len(str):                         # each iteration will read one entire encoded word
            j = i                                   # assign 2nd pointer (to get the integer from encoded) and start from 1st
            while str[j] != "#"                     # keep incrementing j till we reach "#" 
                j += 1
            length = int(str[i:j])                  # store the integer in this varirable as int

            res.append(str[j+ 1 : j + 1 + length])  # j+1 => the 1st character(alphabet) in the word : end of the string
            i = j + 1 + length                      # update 1st pointer i to end of the string

        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # iterating through the input array once to get frequencies
        for n in nums:
            count[n] = 1 + count.get(n, 0)   # count the frequency of each number

        # bucket sort to organize numbers based on their frequencies
        for n, c in count.items():
            freq[c].append(n)                # numbers from the input array are placed in the indexes of the freq list

        res = []   # an array of the results that we will be returning
        # collect the top k frequent numbers
        for i in range(len(freq) - 1, 0, -1):            # loop in reverse
            for n in freq[i]:                            # using frequency
                res.append(n)                            # start adding the elements in result
                if len(res) == k:                        # stop once we reached the target k == 2
                    return res

# We used 2 techniques first is dictionary and then bucket sort.
# The dictionary allows us to count the frequency of the input array
# The original array-input will be in the keys, and the frequencies will be stored in the values

# After that, we organize the numbers or keys by the corresponding frequency.
# For example, if the numbers 2 and 5 both appear 3 times in the input list, they would both be in the bucket at freq[3].

# Lastly, the code then iterates over the freq list in reverse order to collect the top k frequent numbers and put them in the result.

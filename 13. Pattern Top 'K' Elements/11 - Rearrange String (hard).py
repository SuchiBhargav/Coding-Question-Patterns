'''
Problem Statement 
Given a string, find if its letters can be rearranged in such a way that no two same characters ome next to each other.

Example 1:

Input: "aappp"
Output: "papap"
Explanation: In "papap", none of the repeating characters come next to each other.

Example 2:

Input: "Programming"
Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
Explanation: None of the repeating characters come next to each other.

Example 3:

Input: "aapa"
Output: ""
Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".
'''

# mycode
import collections
from heapq import *


def rearrange_string(str):
    charFrequencyMap = collections.Counter(str)

    maxHeap = []
    for char, frequency in charFrequencyMap.items():
        heappush(maxHeap, (-frequency, char))

    previousChar, previousFrequency = None, 0
    resultString = []
    while maxHeap:
        frequency, char = heappop(maxHeap)
        resultString.append(char)
        if previousChar and -previousFrequency > 0:
            heappush(maxHeap, (previousFrequency, previousChar))
        previousChar = char
        previousFrequency = frequency + 1  # decrement the frequency

    return ''.join(resultString) if len(resultString) == len(str) else ""



def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()

# answer
from heapq import *


def rearrange_string(str):
    charFrequencyMap = {}
    for char in str:
        charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

    maxHeap = []
    # add all characters to the max heap
    for char, frequency in charFrequencyMap.items():
        heappush(maxHeap, (-frequency, char))

    previousChar, previousFrequency = None, 0
    resultString = []
    while maxHeap:
        frequency, char = heappop(maxHeap)
        # add the previous entry back in the heap if its frequency is greater than zero
        if previousChar and -previousFrequency > 0:
            heappush(maxHeap, (previousFrequency, previousChar))
        # append the current character to the result string and decrement its count
        resultString.append(char)
        previousChar = char
        previousFrequency = frequency + 1  # decrement the frequency

    # if we were successful in appending all the characters to the result string, return it
    return ''.join(resultString) if len(resultString) == len(str) else ""


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()

'''
Time complexity 
The time complexity of the above algorithm is O(N*logN) where ‘N’ is the number of characters in the input string.

Space complexity 
The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ characters in the HashMap.
'''

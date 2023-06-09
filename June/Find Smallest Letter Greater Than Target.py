# Find Smallest Letter Greater Than Target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        for i in letters:
            if ord(i[0]) > ord(target[0]):
                return i
        return letters[0]
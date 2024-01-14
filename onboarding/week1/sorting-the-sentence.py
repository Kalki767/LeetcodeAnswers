class Solution:
    def sortSentence(self, s: str) -> str:
        original = s.split() #splitting it into a list
        n= len(original)
        reconstruct = [""]*n #for storing the reconstructed
        for i in range(n):
            word = original[i]
            index = int(word[-1]) #extracting the index
            reconstruct[index-1]=word[:-1] #removing the index
        return " ".join(reconstruct)
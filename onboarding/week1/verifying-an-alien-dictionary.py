class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_Index = {c:i for i,c in enumerate(order)}
        for i in range(len(words)-1):
            word1,word2 = words[i],words[i+1]
            for j in range(len(word1)):
                if j==len(word2):   #if word2 is a prefix of word1 then it's not verified
                    return False
                if word1[j]!=word2[j]:
                    if order_Index[word2[j]]<order_Index[word1[j]]: #if the order of the word2 is less than word1 
                        return False
                    break
        return True
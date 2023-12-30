class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timetolive = timeToLive
        self.tokenMap = {} # creating a hashmap to map the specific values with their current time

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenMap[tokenId] = currentTime #adding an element to our hashmap

    def renew(self, tokenId: str, currentTime: int) -> None:
        # checking if the tokenId exists in our map and if it's not expired
        if tokenId in self.tokenMap and self.tokenMap[tokenId]+self.timetolive>currentTime:
            self.tokenMap[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count_unexpired =0
        for key,value in self.tokenMap.items(): #counting unexpired elements
            if value+self.timetolive>currentTime:
                count_unexpired+=1
        return count_unexpired


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
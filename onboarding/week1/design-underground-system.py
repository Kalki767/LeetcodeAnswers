class UndergroundSystem:

    def __init__(self):
        # a person is registered with id as a key and start station and time as value
        self.checkInMap = {} #id->[start,t]
        # we will keep track of how many people travel the same distance and the total time taken by them using the start and the end as akey
        self.totalMap = {} #(start,end)->[totaltime,count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        #when a person is checked in he is registered in Checkinmap
        self.checkInMap[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # when a person is checked out the time is calculated and number of peoples who traveled through that path would be incremented by 1
        startStation, time = self.checkInMap[id]
        route = (startStation,stationName)
        if route not in self.totalMap:
            self.totalMap[route]=[0,0]
        self.totalMap[route][0]+=t-time
        self.totalMap[route][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        #we will unzip our totalmap to find the total time taken and the number of users who traveled the same path
        totaltime, number = self.totalMap[(startStation,endStation)]
        return totaltime/number


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
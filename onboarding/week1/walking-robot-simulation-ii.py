class Robot:

        def __init__(self, width: int, height: int):
            self.x_at = 0
            self.y_at = 0
            self.w = width
            self.h = height
            self.x = 1
            self.y = 0
            self.Direction = ["East", "North", "West", "South"]
            self.Dir = 0

        def swap(self, x, y):
            x, y = y, x
            x *= -1
            return (x, y)

        def step(self, num: int) -> None:
            num%=(self.w-1+self.h-1)*2
            if num==0:
                num+=(self.w-1+self.h-1)*2
            for i in range(num):
                next_x,next_y=self.x_at+self.x,self.y_at+self.y
                while not(0<=next_x<self.w and 0<=next_y<self.h):
                    self.x,self.y = self.swap(self.x,self.y)
                    next_x, next_y = self.x_at + self.x, self.y_at + self.y
                    self.Dir+=1
                self.x_at,self.y_at = next_x,next_y
        def getPos(self) -> list[int]:

            return [ self.x_at,self.y_at]

        def getDir(self) -> str:
            return self.Direction[self.Dir % 4]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
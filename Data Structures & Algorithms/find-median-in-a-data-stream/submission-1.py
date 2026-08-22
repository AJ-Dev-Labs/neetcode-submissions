class MedianFinder:

    def __init__(self):
        self.data = []

        

    def addNum(self, num: int) -> None:
        self.data.append(num)
        self.data.sort()

        

    def findMedian(self) -> float:
        nums = len(self.data)
        if nums == 1:
            return self.data[0]
        if nums % 2 == 0:
            m1 = nums//2
            m2 = m1-1
            return (self.data[m1]+self.data[m2])/2
        else:
            m = nums//2
            return self.data[m]
        
        
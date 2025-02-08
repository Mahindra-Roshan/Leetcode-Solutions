class NumberContainers:

    def __init__(self):
        self.indexmonitor = {}
        self.numbermonitor = defaultdict(SortedList)
        

    def change(self, index: int, number: int) -> None:
        if index in self.indexmonitor:
            oldnumber = self.indexmonitor[index]
            self.numbermonitor[oldnumber].discard(index)
            if not self.numbermonitor[oldnumber]:
                del self.numbermonitor[oldnumber]

        self.indexmonitor[index] = number
        self.numbermonitor[number].add(index)
        

    def find(self, number: int) -> int:
        if number not in self.numbermonitor or not self.numbermonitor[number]:
            return -1
        return self.numbermonitor[number][0]
        

#here i learnt this one and initially i solved it with set but using the set and finally finding it by traversing through every index to find the minimum got me a error TLE
#so i used a sortedlist and so i can return the first by using index 0
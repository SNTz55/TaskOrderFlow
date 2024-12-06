import time

class Task:
    def __init__(self, name: str, priority: int, deadline: int) -> None:
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.updateTime()

    def updateTime(self) -> None:
        self.now = int(time.time())
        self.score = self.calcScore()
        print(self.score)

    def calcScore(self) -> float:
        trem = (self.deadline - self.now) / 86400
        dscore = max(0, 100 - trem)
        pscore = 100 - (max(0, min(100, 25 * self.priority)))

        score = dscore * 0.7 + pscore * 0.3
        return score

if __name__ == '__main__':
    a = Task("amogus", 0, int(time.time()) + 8640000)

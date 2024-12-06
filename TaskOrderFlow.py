from datetime import datetime
class Task:
    today = datetime.today()

    def __init__(self, name: str, deadline: str, priority: int):
        self.name = name
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.priority = priority

    def calculateScore(self):

        # TODO: Find a better scoring system
        daysLeft = (self.deadline - self.today).days

        dscore = 100 - daysLeft
        pscore = 100 - 33.3333333 * self.priority
        difficulty = None


        score = dscore * 0.7 + pscore * 0.3
        score += 30 if daysLeft <= 0 else 0

        return score

    def test(self):
        print("Name: ", self.name,
              "\nDeadline: ", self.deadline,
              "\nPriority: ", self.priority,
              "\nscore: ", self.calculateScore())

if __name__ == '__main__':
    t = Task('amogus', "2024-12-31", 0)
    t.test()

import time

class TaskOrderFlow:
    now = int(time.time())

    def test(self):
        print(now)

if __name__ == '__main__':
    a = TaskOrderFlow()
    a.test()

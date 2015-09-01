from fenglib import *

@singleton.singleton
class Cell():
    def __init__(self):
        self.count = 0

    def IncCount(self):
        self.count += 1

if __name__ == "__main__":
    c0 = Cell()
    assert c0.count == 0
    c0.IncCount()
    assert c0.count == 1
    c1 = Cell()
    assert c1.count == 1

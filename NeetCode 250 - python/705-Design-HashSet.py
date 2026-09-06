class MyHashSet:

    def __init__(self):
        self.myHashSet = []

    def add(self, key: int) -> None:
        myHashSet = self.myHashSet
        myHashSet.append(key)

    def remove(self, key: int) -> None:
        myHashSet = self.myHashSet
        while self.contains(key):
            myHashSet.remove(key)

    def contains(self, key: int) -> bool:
        x = self.myHashSet.count(key)
        if x > 0:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
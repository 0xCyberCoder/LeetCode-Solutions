class MyHashSet:

    def __init__(self):
        self.myHashSet = []

    def add(self, key: int) -> None:
        myHashSet = self.myHashSet
        myHashSet.append(key)

    def remove(self, key: int) -> None:
        myHashSet = self.myHashSet
        x = self.myHashSet.count(key)
        while x > 0:    
            myHashSet.remove(key)
            x -= 1

    def contains(self, key: int) -> bool:
        x = self.myHashSet.count(key)
        return bool(x)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
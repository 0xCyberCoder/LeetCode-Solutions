class MyHashMap:

    def __init__(self):
        self.myKey = []
        self.myValue = []

    def put(self, key: int, value: int) -> None:
        myKey = self.myKey
        myValue = self.myValue

        if key not in myKey:
            myKey.append(key)
            myValue.append(value)
        else:
            i = myKey.index(key)
            myValue[i] = value

    def get(self, key: int) -> int:
        myKey = self.myKey
        myValue = self.myValue

        if key not in myKey:
            return -1
        else:
            i = myKey.index(key)
            return myValue[i]

    def remove(self, key: int) -> None:
        myKey = self.myKey
        myValue = self.myValue

        if myKey.count(key) > 0:
            i = myKey.index(key)
            myKey.pop(i)
            myValue.pop(i)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
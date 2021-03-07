class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        for data in self.storage:
            if data[0] == key:
                data[1] = value
                return
        self.storage.append([key,value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for data in self.storage:
            if data[0] == key:
                return data[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for i in range(0,len(self.storage)):
            if self.storage[i][0] == key:
                self.storage.pop(i)
                return
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


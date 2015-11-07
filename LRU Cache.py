class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.queue=[]
        self.cache={}
    def get(self,key):
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        else:
            return -1
    def set(self,key,value):
        if key in self.cache:
            self.cache[key]=value
            self.queue.remove(key)
            self.queue.append(key)
        else:
            if len(self.queue)==self.capacity:
                todel=self.queue.pop(0)
                del self.cache[todel]
            self.queue.append(key)
            self.cache[key]=value
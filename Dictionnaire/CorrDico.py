class Dico:
    def __init__(self):
         self.keys = []
         self.values = []
    
    def get(self, key):
        for i in range(len(self.keys)):
            if(self.keys[i] == key):
                return self.values[i]
        return None

    def pop(self, key):
        ret = None
        for i in range(len(self.keys)):
            if(self.keys[i]== key):
                ret = self.values[i]
                del self.keys[i]
                del self.values[i]
                break
        return ret

    def update(self, key, value):
        for i in range(len(self.keys)):
            if(self.keys[i] == key):
                self.values[i] = value
        self.keys.append(key)
        self.values.append(value)

dc = Dico()
dc.update("kiko",75)
print(dc.get("kiko"))
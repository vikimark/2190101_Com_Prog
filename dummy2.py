class player: 
    def __init__(self, id): 
        self.id = id 
        self.item = [] 
        self.pay = 0 
class item: 
    def __init__(self, id): 
        self.id = id 
        self.price = 0 
        self.yesno = False 
        self.owner = ['n'] 

items = {}

for i in range(10):
    items[str(i)] = item(str(i))

print(items)
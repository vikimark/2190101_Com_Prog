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
 
def datainput(): 
    for j in range(int(input())): 
        y = [i for i in input().split()] 
        if len(y) == 4: 
            y[3] = int(y[3]) 
        l.append(y) 
        if l[j][1] not in playerindex: 
            playerindex.append(l[j][1]) 
        if l[j][2] not in itemindex: 
            itemindex.append(l[j][2]) 
    playerindex.sort() 
    itemindex.sort() 
    for j in playerindex: 
        playerlist.append(player(j)) 
    for j in itemindex: 
        itemlist.append(item(j)) 
def processing(): 
    for j in l: 
        p = playerindex.index(j[1]) 
        i = itemindex.index(j[2]) 
        if j[0] == 'B': 
            if j[3] > itemlist[i].price: 
                if len(itemlist[i].owner) == 1: 
                    itemlist[i].yesno = True 
                if itemlist[i].yesno == True: 
                    itemlist[i].owner.append([j[1], j[3]]) 
                    itemlist[i].price = j[3] 
            elif j[3] <= itemlist[i].price: 
                ins = 1 
                for q in range(1, len(itemlist[i].owner)): 
                    if j[3] > itemlist[i].owner[q][1]: 
                        ins += 1 
                        pass 
                    elif j[3] <= itemlist[i].owner[q][1]: 
                        itemlist[i].owner.insert(ins, [j[1], j[3]])     
                        break   
        elif j[0] == 'W': 
            temp = [] 
            for o in itemlist[i].owner[-1:0:-1]: 
                if o[0] == j[1]: 
                    temp.append(o) 
            for o in temp: 
                itemlist[i].owner.remove(o) 
            if len(itemlist[i].owner) == 1: 
                itemlist[i].price = 0 
                itemlist[i].yesno = False 
            else: 
                itemlist[i].price = itemlist[i].owner[-1][1]  
    for i in itemlist: 
        if i.yesno: 
            p = playerlist[playerindex.index(i.owner[-1][0])] 
            p.item.append(i.id) 
            p.pay += i.owner[-1][1] 
def announcement(): 
    for p in playerlist: 
        if p.pay == 0 : 
            print(p.id + ": $0") 
        else: 
            print("{}: ${} ->{}".format(p.id, p.pay, " ".join(p.item))) 
 
# Variables 
l = [] 
playerindex = []
playerlist = []
itemindex = []
itemlist = []
 
datainput() 
processing() 
announcement()
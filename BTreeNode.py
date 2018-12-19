import BTreeKey

class BTreeNode:
    def __init__(self,isRoot,isLeaf,father,key):
        self.isRoot = isRoot
        self.isLeaf = isLeaf              
        self.father = father
        self.keyList = [key,None,None]
    
    def isLeaf(self):
        for i in range (0,self.getNumKeys()):
            if not self.keyList[i].atLeaf():
                return False
        return True

    def addKey(self,key):
        if keyList[1] is None:
            self.keyList[1] = key
        else:
            self.keyList[2] = key
        self.sortKeyList()

    def sortKeyList(self):
        if len(self.keyList) == 2:
            if self.keyList[0].getKey() > self.keyList[1].getKey():
                tempKey = self.keyList[0]
                self.keyList[0] = self.keyList[1]
                self.keyList[1] = tempKey
        else:
            keyList.sort(self.compare) 

    def compare(self,key1,key2):
        if key1.getKey() < key2.getKey():
            return -1
        elif key1.getKey() > key2.getKey():
            return 1
        else:
            return 0

    def getFather(self):
        return self.father

    def setFather(self,father):
        self.father = father

    def getKey(self,index):
        return self.keyList[index]

    def getNumKeys(self):
        cont = 0
        for i in range (0,3):
            if not self.keyList[i] == None:
                cont += 1
        return cont

    def contains(self,key):
        for i in range (0,4):
            if(key == self.keyList[i].getKey()):
                return i
        return -1

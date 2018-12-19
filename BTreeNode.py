import BTreeKey

class BTreeNode:
    def __init__(self,isRoot,isLeaf,rightSon,leftSon,father,key):
        self.isRoot = isRoot
        self.isLeaf = isLeaf            
        self.rightSon = rightSon
        self.leftSon = leftSon        
        self.father = father
        self.keyList = [key,None,None]
    
    def addKey(self,key):
        if keyList[1] is None:
            self.keyList[1] = key
        else
            self.keyList[2] = key

    def getFather(self):
        return self.father

    def setFather(self,father):
        self.father = father

    def getKey(self,index):
        return self.keyList[index]

    def getNumKeys(self):
        return len(keyList)

    def contains(self,key):
        for i in range (0,4):
            if(key == self.keyList[i].getKey()):
                return i
        return -1

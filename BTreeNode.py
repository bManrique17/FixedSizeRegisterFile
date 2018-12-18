import BTreeKey

class BTreeNode:
    def __init__(self,isRoot,isLeaf,rightSon,leftSon,key):
        self.isRoot = isRoot
        self.isLeaf = isLeaf            
        self.rightSon = rightSon
        self.leftSon = leftSon        
        self.keyList = [key,0,0,0]
    
    def addKey(self,key):
        self.keyList.append(key)

    def getKey(self,index):
        return self.keyList[index]

    def contains(self,key):
        for i in range (0,4):
            if(key == self.keyList[i].getKey()):
                return i
        return -1

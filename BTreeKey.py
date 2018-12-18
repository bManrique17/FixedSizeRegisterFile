class BTreeKey:
    def __init__(self,key,filePosition,rightSon,leftSon):
        self.key = key
        self.filePosition = filePosition
        self.rightSon = rightSon
        self.leftSon = leftSon    

    def getRightSon(self):
        return self.rightSon

    def getLeftSon(self):
        return self.leftSon

    def getFilePosition(self):
        return self.filePosition

    def getKey(self):
        return self.key
      

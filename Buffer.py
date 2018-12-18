class Buffer:
    def __init__(self):

    def setMetadata(self,file,objectIndicator):
        self.objectIndicator = objectIndicator
        dataLine = file.readline(objectIndicator)
        infoObjectList = dataLine.split(",")
        self.numAtributes = int(infoObjectList[1])
        for i in range(0,self.numAtributes+1):
            self.listAtributesSize = int(infoObjectList[i+2])

    def setActualObject(self,object):
        self.actualObject = object

    def getActualObjectKey(self):
        return self.actualObject.getKey()

    def getRegSize(self):
        return self.regSize

    def read(self,file):
        dataLine = file.read(self.listAtributesSize[len(listAtributesSize)-1])
        cont = 0
        indexFlag = 0
        atributes = [0,0,0,0,0,0,0,0,0]
        for i in range (0,self.numAtributes):
            atributes[cont] = dataLine[indexFlag:indexFlag+listAtributesSize[cont]]
            indexFlag = indexFlag+listAtributesSize[cont]
            cont = cont+1
            atributes[cont] = atributes[cont].rstrip()
        if self.objectIndicator == 1:
            self.actualObject = Personaje(atributes[0],atributes[1],atributes[2],atributes[3])
        elif self.objectIndicator == 2:
            self.actualObject = PartidaGuardada(atributes[0],atributes[1],atributes[2])
        elif self.objectIndicator == 3:
            self.actualObject = Bitacora(atributes[0],atributes[1],atributes[2],atributes[3],atributes[4])
        else:
            self.actualObject = Item(atributes[0],atributes[1],atributes[2])

    def write(self,file):
        if self.objectIndicator == 1:            
            file.write(getActualObject().getNombre()+" "*len(self.listAtributesSize[0]-getActualObject().getNombre()) +
                getActualObject().getDamage()+" "*len(self.listAtributesSize[0]-getActualObject().getDamage()) +
                getActualObject().getDefense()+" "*len(self.listAtributesSize[0]-getActualObject().getDefense()) +
                getActualObject().getVida()+" "*len(self.listAtributesSize[0]-getActualObject().getVida()))
        elif self.objectIndicator == 2:
            file.write(getActualObject().getNombre()+" "*len(self.listAtributesSize[0]-getActualObject().getNombre()) +
                getActualObject().getDamage()+" "*len(self.listAtributesSize[0]-getActualObject().getDamage()) +
                getActualObject().getDefense()+" "*len(self.listAtributesSize[0]-getActualObject().getDefense()) +
                getActualObject().getVida()+" "*len(self.listAtributesSize[0]-getActualObject().getVida()))
        elif self.objectIndicator == 3:
            file.write(getActualObject().getNombre()+" "*len(self.listAtributesSize[0]-getActualObject().getNombre()) +
                getActualObject().getDamage()+" "*len(self.listAtributesSize[0]-getActualObject().getDamage()) +
                getActualObject().getDefense()+" "*len(self.listAtributesSize[0]-getActualObject().getDefense()) +
                getActualObject().getVida()+" "*len(self.listAtributesSize[0]-getActualObject().getVida()))
        else:
            file.write(getActualObject().getNombre()+" "*len(self.listAtributesSize[0]-getActualObject().getNombre()) +
                getActualObject().getDamage()+" "*len(self.listAtributesSize[0]-getActualObject().getDamage()) +
                getActualObject().getDefense()+" "*len(self.listAtributesSize[0]-getActualObject().getDefense()) +
                getActualObject().getVida()+" "*len(self.listAtributesSize[0]-getActualObject().getVida()))
        file.write()

    def equals(self,buffer):
        return self.getActualObjectKey() == buffer.getActualObjectKey()
    
    def erase(self,file):
        deletedKey = " "*self.listAtributesSize[0]
        file.write(deletedKey)



    
    
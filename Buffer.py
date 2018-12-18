class Buffer:
    def __init__(self):

    def setMetadata(self,file,objectIndicator):
        self.objectIndicator = objectIndicator
        dataLine = file.readline(objectIndicator)
        infoObjectList = dataLine.split(",")
        self.numAtributes = int(infoObjectList[1])
        for i in range(0,self.numAtributes+1):
            self.listAtributesSize = int(infoObjectList[i+2])
        self.regSize = listAtributesSize[len(listAtributesSize)-1]

    def setRootKey(self,key):
        self.rootKey = key

    def getRootKey(self,key):
        self.rootKey = key

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
            file.write(getActualObject().getNombre()+" "*( self.listAtributesSize[0]-len(getActualObject().getNombre()) ) +
                getActualObject().getDamage()+" "*( self.listAtributesSize[1]-len(getActualObject().getDamage()) ) +
                getActualObject().getDefense()+" "*( self.listAtributesSize[2]-len(getActualObject().getDefense()) ) +
                getActualObject().getVida()+" "*( self.listAtributesSize[3]-len(getActualObject().getVida()) ) )
        elif self.objectIndicator == 2:
            file.write(getActualObject().getNombrePartida()+" "*( self.listAtributesSize[0]-len(getActualObject().getNombrePartida()) ) +
                getActualObject().getMisionesCompletadas()+" "*( self.listAtributesSize[1]-len(getActualObject().getMisionesCompletadas()) ) +
                getActualObject().getArmadurasObtenidas()+" "*( self.listAtributesSize[2]-len(getActualObject().getArmadurasObtenidas()) ) )                
        elif self.objectIndicator == 3:
            file.write(getActualObject().getNombrePartida()+" "*( self.listAtributesSize[0]-len(getActualObject().getNombrePartida()) ) +
                getActualObject().getFecha()+" "*( self.listAtributesSize[1]-len(getActualObject().getFecha()) ) +
                getActualObject().getHoraEntrada()+" "*( self.listAtributesSize[1]-len(getActualObject().getHoraEntrada()) ) +
                getActualObject().getHoraSalida()+" "*( self.listAtributesSize[1]-len(getActualObject().getHoraSalida()) ) +                
                getActualObject().getHoraInsert()+" "*( self.listAtributesSize[3]-len(getActualObject().getHoraInsert()) ) )
        else:
            file.write(getActualObject().getNombre()+" "*( self.listAtributesSize[0]-len(getActualObject().getNombre()) ) +
                getActualObject().getNombreMonstruo()+" "*( self.listAtributesSize[1]-len(getActualObject().getNombreMonstruo()) ) +
                getActualObject().getTipo()+" "*( self.listAtributesSize[2]-len(getActualObject().getTipo()) ) )        
    
    def erase(self,file):        
        file.write(" "*self.listAtributesSize[0])    
    
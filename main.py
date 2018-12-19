import TDAFile
import Buffer
import Bitacora
import Item
import PartidaGuardada
import Personaje

file = TDAFile.TDAFile("test.txt")
file.openFile()
Manrique = Personaje.Personaje("Bryan",1,1,1)
bufferPersonajes = Buffer.Buffer("MetadataFile.txt",0)
bufferPersonajes.setActualObject(Manrique)
file.insert(bufferPersonajes)
for i in range (0,6):    
    Manrique = Personaje.Personaje("Bryan"+str(i),1+i,1+i,1+i)
    bufferPersonajes.setActualObject(Manrique)
    file.insert(bufferPersonajes)

Manrique = Personaje.Personaje("Bryan",4,4,4)
objectttt = file.find(bufferPersonajes)
if objectttt is not None:
    print (objectttt[1].getDefense())
file.closeFile()




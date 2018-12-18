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
print(file.find(bufferPersonajes)[1].getDefense())
file.closeFile()




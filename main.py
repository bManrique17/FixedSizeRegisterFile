import TDAFile
import Buffer
import Nicolle

print("hola")
nicolle = Nicolle.Nicolle("aaaaa","bbbbb","kkkkk")
file = TDAFile.TDAFile("test.txt")
buffer = Buffer.Buffer()
buffer.setActualObject(nicolle)
file.createFile()
file.openFileW()
file.insert(buffer)
file.closeFile()




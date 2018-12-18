#/******************************************************
#Nombre de la clase: TDAFile
#
#Descripcion:        Plantilla de las operaciones elem-
#                    entales de un archivo.
#
#Clase:              Estructura de Datos II
#
#Fecha:              9 de diciembre del 2018
#
#Autor:              Bryan Manrique Amador Mena
#******************************************************/

import os
import Buffer
import BTreeNode
import BTreeKey

class TDAFile:
    def __init__(self,fileName):
        self.fileName = fileName        
        self.root = None

    def createFile(self,fileName):
        self.file = open(fileName,'w')
        self.file.close()
    def createFile(self):
        self.file = open(self.fileName,'w')
        self.file.close()        
    def openFile(self):
        self.file = open(self.fileName,'a+')    
    def closeFile(self):
        self.file.close()
    def deleteFile(self):
        os.remove(fileName)
    def insert(self,buffer):
        if self.root is None:            
            self.root = BTreeNode.BTreeNode(True,True,None,None,BTreeKey.BTreeKey(buffer.getActualObjectKey(),0,None,None))
        self.file.seek(self.file.tell())
        buffer.write(self.file)
    def update(self,bufferOld,bufferNew):
        position = find(bufferOld)[0]
        if position != -1:
            self.file.seek(position)
            bufferNew.write(self.file)
    def find(self,buffer):
        found = False
        actualNode = self.root
        while True:            
            positionKey = actualNode.contains(buffer.getActualObjectKey())            
            if positionKey != -1:                                
                self.file.seek(actualNode.getKey(positionKey).getFilePosition())                
                return [positionKey,buffer.read(self.file)]
        
    def deleteReg(self,buffer):
        toRemove = find(buffer)[0]
        if toRemove != -1:
            self.file.seek(toRemove)
            buffer.erase(self.file)


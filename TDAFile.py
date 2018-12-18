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

class TDAFile:
    def __init__(self,fileName):
        self.fileName = fileName        
    
    def createFile(self,fileName):
        self.file = open(fileName,'w')
        self.file.close()
    def createFile(self):
        self.file = open(self.fileName,'w')
        self.file.close()        
    def openFileW(self):
        self.file = open(self.fileName,'w')
    def openFileR(self):
        self.file = open(self.fileName,'r')
    def closeFile(self):
        self.file.close()
    def deleteFile(self):
        os.remove(fileName)
    def insert(self,buffer):
        if self.rootKey is None:
            self.rootKey = bTreeKey(True,True,None,None,buffer.getActualObject().getKey())
        self.file.seek(self.file.tell())
        buffer.write(self.file)
    def update(self,bufferOld,bufferNew):
        position = find(bufferOld)[0]
        if position != -1:
            file.seek(position)
            bufferNew.write(file)
    def find(self,buffer):
        found = False
        actualNode = self.rootKey
        while True:
            positionKey = actualNode.contains(buffer.getActualObjectKey())
            if actualNode.contains(buffer.getActualObjectKey()) != -1:
                file.seek(positionKey)
                return [positionKey,buffer.read(file)]
                
    def deleteReg(self,buffer):
        toRemove = find(buffer)[0]
        if toRemove != -1:
            file.seek(toRemove)
            buffer.erase(file)

    class bTreeKey:
        def __init__(self,key,filePosition,rightBrother,leftBrother)
            self.key = key
            self.filePosition = filePosition
            self.rightBrother = rightBrother
            self.leftBrother = leftBrother                

        def getFilePosition():
            return filePosition

    class bTreeNode:
        def __init__(self,isRoot,isLeaf,rightSon,leftSon,key):
            self.isRoot = isRoot
            self.isLeaf = isLeaf            
            self.rightSon = rightSon
            self.leftSon = leftSon
            self.keyList = [key,0,0]
        
        def contains(self,key):
            if key == keyList[0]:
                return keyList[0].getFilePosition()
            elif key == keyList[1]:
                return keyList[1].getFilePosition()
            elif key == keyList[2]:
                return keyList[2].getFilePosition()
            else:
                return -1
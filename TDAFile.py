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
        self.file.seek(self.file.tell())
        buffer.write(self.file)
    def update(self,bufferOld,bufferNew):
        position = find(bufferOld)
        if(position != -1):
            self.file.seek(position)
            bufferNew.write(self.file)
    def find(self,buffer):
        
        return buffer.getActualObject()
    def deleteReg(self,buffer):
        buffer.erase()

    class bTreeNode:
    def __init__(self,isRoot,isLeaf,rightBrother,leftBrother,rightSon,leftSon):
        self.isRoot = isRoot
        self.isLeaf = isLeaf
        self.rightBrother = rightBrother
        self.leftBrother = leftBrother
        self.rightSon = rightSon
        self.leftSon = leftSon
        self.keyList = [0,0,0]
    
    #def insertKey(self,key):
        #self.keyList.insert
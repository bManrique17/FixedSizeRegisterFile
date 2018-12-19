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
        toInsertKey = buffer.getActualObjectKey()
        if self.root is None:            
            newKey = BTreeKey.BTreeKey(toInsertKey,0,None,None,self.root)
            self.root = BTreeNode.BTreeNode(True,True,None,newKey)
            buffer.addObjectToQueue()
        else:
            actualNode = self.root
            if actualNode.isLeaf() == True and actualNode.getNumKeys() < 3:
                actualNode.addKey(BTreeKey.BTreeKey(buffer.getActualObject(),self.file.tell()/buffer.getRegSize(),None,None,actualNode))
            else:
                while not actualNode.isLeaf():
                    if actualNode.getKey(0).getKey() > toInsertKey:
                        actualNode = actualNode.getKey(0).getLeftSon()
                    elif actualNode.getKey(0).getKey() < toInsertKey and actualNode.getKey(1).getKey() > toInsertKey:
                        actualNode = actualNode.getKey(0).getRightSon()
                    elif actualNode.getKey(1).getKey() < toInsertKey and actualNode.getKey(2).getKey() > toInsertKey:
                        actualNode = actualNode.getKey(1).getRightSon()
                    else:
                        actualNode = actualNode.getKey(2).getRightSon()
                if actualNode.isLeaf() and actualNode.getNumKeys() < 3:
                    actualNode.addKey(BTreeKey.BTreeKey(buffer.getActualObject(),self.file.tell()/buffer.getRegSize(),None,None,actualNode))
                else:
                    seekNode(actualNode)        

    def seekNode(self,node,key):
        if node.getNumKeys() == 2:
            newKey = BTreeKey.BTreeKey(key,self.file.tell()/buffer.getRegSize(),None,None,node)
            node.addKey(newKey)
            toPromoveKey = node.getKey(1)
            toPromoveKey.setLeftSon(BTreeNode.BTreeNode(False,node.getKey(0).atLeaf(),toPromoveKey,node.getKey(1)))
            toPromoveKey.setRightSon(BTreeNode.BTreeNode(False,node.getKey(2).atLeaf(),toPromoveKey,node.getKey(2)))
            if toPromoveKey.getOwnNode().getFather() == None:
                self.root = BTreeNode.BTreeNode(True,False,None,toPromoveKey)
            else:                
                seekNode(toPromoveKey.getOwnNode().getFather(),toPromoveKey)


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


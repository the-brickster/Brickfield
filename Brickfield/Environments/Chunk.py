'''
Created on Jun 5, 2014

@author: lando
@summary: Attempt at block game taken from:
http://studentgamedev.blogspot.no/2013/08/unity-voxel-tutorial-part-1-generating.html
'''
import CubeModelGenerator
import numpy as np
from panda3d.core import *
from numpy import dtype
from random import randint

class Chunk(object):
    '''
    Basic Chunk
    '''
    chunkSize = 0
    chunkX=0
    chunkY=0
    chunkZ=0

    def __init__(self, world):
        '''
        Constructor
        '''
        self.worldRef = world

    def GenerateMesh(self, renderNode):
        '''
        @todo: Add renderNode param... done
        '''
        self.cubeModel = CubeModelGenerator.MeshGenerator("Chunk"+str(self))

        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        counter = 0
        for x in range(0, self.chunkSize):
            for y in range(0, self.chunkSize):
                for z in range(0, self.chunkSize):
                    

                    if(self.Block(x,y,z) != 0):
                        #block is a solid
                        if(self.Block(x,y+1,z) == 0):
                            self.cubeModel.makeFrontFace(x+self.chunkX,y+self.chunkY,z+self.chunkZ, [r,g,b,1])

                        if(self.Block(x,y-1,z) == 0):
                            self.cubeModel.makeBackFace(x+self.chunkX,y+self.chunkY,z+self.chunkZ, [r,g,b,1])

                        if(self.Block(x+1,y,z) == 0):
                            self.cubeModel.makeRightFace(x+self.chunkX,y+self.chunkY,z+self.chunkZ, [r,g,b,11])

                        if(self.Block(x-1,y,z) == 0):
                            self.cubeModel.makeLeftFace(x+self.chunkX,y+self.chunkY,z+self.chunkZ, [r,g,b,1])

                        if(self.Block(x,y,z+1) == 0):
                            counter+=1
                            self.cubeModel.makeTopFace(x+self.chunkX,y+self.chunkY,z+self.chunkZ, [r,g,b,1])

                        if(self.Block(x,y,z-1) == 0):
                            self.cubeModel.makeBottomFace(x+self.chunkX,y+self.chunkY,z+self.chunkZ, [r,g,b,1])

        #print "Made Chunk with: "+str(counter)+" faces"
        self.np = renderNode.attachNewNode(self.cubeModel.getGeomNode())
        #self.np.set_pos(self.chunkX,self.chunkY,self.chunkZ)


    def Block(self,x,y,z):
        return self.worldRef.Block(x+self.chunkX,y+self.chunkY,z+self.chunkZ)


    def Update(self):
        pass

# if __name__ == '__main__':
#     chunk = Chunk("test")
#     chunk.render()
#     run()

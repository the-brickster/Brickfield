'''
Created on May 6, 2014

@author: TaeZ (from panda3d forums), modified by lando
'''
from panda3d.core import Texture, GeomNode, GeomVertexFormat, GeomVertexData, Geom, GeomTriangles, GeomVertexFormat,GeomVertexWriter, Vec3, Vec4, Point3
import time

def CalcSufaceNormal(myVec):
    myVec.normalize()
    return myVec

def convertToRGBA(rVal, gVal, bVal, alpha):
    '''Converts 0-255 RGBA values to Panda3d RGBA values'''
    return (rVal/float(255),gVal/float(255),bVal/float(255),alpha)

class MeshGenerator(object):
    '''
    Generates a cube mesh
    '''


    def __init__(self, name = 'Mesh'):
        '''
        Constructor
        '''
        self.name = name
        self.finished = False

        self.format = GeomVertexFormat.getV3n3c4()
        self.vertexData = GeomVertexData(name, self.format, Geom.UHStream)

        self.mesh = Geom(self.vertexData)
        self.triangles = GeomTriangles(Geom.UHStream)
        self.triangleData = self.triangles.modifyVertices()

        self.vertex = GeomVertexWriter(self.vertexData, 'vertex')
        self.normal = GeomVertexWriter(self.vertexData, 'normal')
        self.color = GeomVertexWriter(self.vertexData, 'color')
        #self.texcoord = GeomVertexWriter(self.vertexData, 'texcoord')

        self.faceCount = 0


    def makeFace(self, x1, y1, z1, x2, y2, z2, color):

        if x1 != x2:

            self.vertex.addData3f(x1, y1, z1)
            self.vertex.addData3f(x2, y1, z1)
            self.vertex.addData3f(x2, y2, z2)
            self.vertex.addData3f(x1, y2, z2)

            vector1 = Vec3(x1, y1, z1)
            vector2 = Vec3(x2, y1, z1)
            vector3 = Vec3(x2, y2, z2)
            
            normalVector1 = vector3-vector1
            normalVector2 = vector2-vector1
            normalVector2.cross(normalVector1)

            self.normal.addData3f(CalcSufaceNormal(normalVector2))
            self.normal.addData3f(CalcSufaceNormal(normalVector2))
            self.normal.addData3f(CalcSufaceNormal(normalVector2))
            self.normal.addData3f(CalcSufaceNormal(normalVector2))

        else:

            self.vertex.addData3f(x1, y1, z1)
            self.vertex.addData3f(x2, y2, z1)
            self.vertex.addData3f(x2, y2, z2)
            self.vertex.addData3f(x1, y1, z2)
            
            vector1 = Vec3(x1, y1, z1)
            vector2 = Vec3(x2, y2, z1)
            vector3 = Vec3(x2, y2, z2)
            
            normalVector1 = vector3-vector1
            normalVector2 = vector2-vector1
            normalVector2.cross(normalVector1)

            self.normal.addData3f(CalcSufaceNormal(normalVector2))
            self.normal.addData3f(CalcSufaceNormal(normalVector2))
            self.normal.addData3f(CalcSufaceNormal(normalVector2))
            self.normal.addData3f(CalcSufaceNormal(normalVector2))

        RGBAVal = convertToRGBA(color[0], color[1], color[2], color[3])
        self.color.addData4f(RGBAVal[0], RGBAVal[1], RGBAVal[2], RGBAVal[3])
        self.color.addData4f(RGBAVal[0], RGBAVal[1], RGBAVal[2], RGBAVal[3])
        self.color.addData4f(RGBAVal[0], RGBAVal[1], RGBAVal[2], RGBAVal[3])
        self.color.addData4f(RGBAVal[0], RGBAVal[1], RGBAVal[2], RGBAVal[3])

        vertexId = self.faceCount * 4

        self.triangles.addVertices(vertexId, vertexId + 1, vertexId + 3)
        self.triangles.addVertices(vertexId + 1, vertexId + 2, vertexId + 3)

        self.faceCount += 1

    def makeFrontFace(self, x, y, z, color):
        self.makeFace(x + 1, y + 1, z - 1, x, y + 1, z, color)

    def makeBackFace(self, x, y, z, color):
        self.makeFace(x, y, z - 1, x + 1, y, z, color)

    def makeRightFace(self, x, y, z, color):
        self.makeFace(x + 1, y, z - 1, x + 1, y + 1, z, color)

    def makeLeftFace(self, x, y, z, color):
        self.makeFace(x, y + 1, z - 1, x, y, z, color)

    def makeTopFace(self, x, y, z, color):
        self.makeFace(x + 1, y + 1, z, x, y, z, color)

    def makeBottomFace(self, x, y, z, color):
        self.makeFace(x, y + 1, z - 1, x + 1, y, z - 1, color)

    def getMesh(self):
        return self.mesh

    def getGeomNode(self):
        if self.finished == False:
            self.triangles.closePrimitive()
            self.mesh.addPrimitive(self.triangles)
            self.finished = True
        geomNode = GeomNode(self.name)
        geomNode.addGeom(self.mesh)
        return geomNode




if __name__ == '__main__':
    mesh = MeshGenerator()
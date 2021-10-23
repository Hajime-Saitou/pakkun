import bpy
from .VertexGroups import VertexGroups
from .Vertices import Vertices
from .Faces import Faces
from .Origin import Origin

class MeshObject(object):
    def __init__(self, name:str):
        object = bpy.data.objects[name]
        if object.type != "MESH":
            raise TypeError("Specify a mesh object.")

        self.object = object
        self.name = name
        self.mesh = self.object.data
        self.origin = Origin(self.object, self)

    @property
    def vertexGroups(self):
        return VertexGroups(self.object)
    
    @property
    def vertices(self):
        return Vertices(self.mesh.vertices, self.origin)

    @property
    def faces(self):
        return Faces(self.mesh.polygons, self.origin)

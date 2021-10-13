import bpy
from mathutils import Vector

class VertexGroup(object):
    def __init__(self, object, name:str):
        self.object = object
        self.name = name

    @property
    def index(self):
        return self.object.vertex_groups.find(self.name)

    @property        
    def vertices(self):
        if self.index < 0:
            return None

        vertices = [ vertex for vertex in self.object.data.vertices if self.index in [ group.group for group in vertex.groups ] ]
        return Vertices(vertices)

class VertexGroups(object):
    def __init__(self, object):
        self.object = object

    def __getitem__(self, key):
        return VertexGroup(self.object, key)

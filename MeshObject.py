import bpy

class MeshObject(object):
    def __init__(self, name:str):
        object = bpy.data.objects[name]
        if object.type != "MESH":
            raise TypeError("Specify a mesh object.")

        self.object = object
        self.name = name
        self.mesh = self.object.data

    @property
    def vertexGroups(self):
        return VertexGroups(self.object)
    
    @property
    def vertices(self):
        return Vertices(self.mesh.vertices, self)

    @property
    def faces(self):
        return Faces(self.object)
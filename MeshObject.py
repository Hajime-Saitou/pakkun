import bpy

class MeshObject(object):
    def __init__(self, objectName:str):
        object = bpy.data.objects[objectName]
        if object.type != "MESH":
            raise TypeError("Specify a mesh object.")
        self.object = object
        self.mesh = self.object.data

    @property
    def vertexGroups(self):
        return VertexGroups(self.object)

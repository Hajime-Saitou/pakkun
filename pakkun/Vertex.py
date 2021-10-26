import bpy
from .Exception.BlenderModeError import BlenderModeError

class Vertex(object):
    def __init__(self, vertex, origin):
        self.vertex = vertex
        self.origin = origin

        self.__setProperty(vertex)

    def __setProperty(self, vertex):
        self.index = vertex.index
        self.co = vertex.co
        self.hide = vertex.hide
        self.normal = vertex.normal
        self.select = vertex.select

    @property
    def serialize(self) -> dict:
        if self.origin.origin.mode != "OBJECT":
            raise BlenderModeError("Blender mode must be set to 'OBJECT'.")

        properties = {}
        properties["index"] = self.index
        properties["co"] = tuple(self.co)
        properties["hide"] = self.hide
        properties["normal"] = self.normal
        properties["select"] = self.select

        if self.origin.belongTo == "VertexGroup":
            properties["weight"] = [ { self.origin.accessor.name: self.weight } ]
        else:
            properties["weight"] = self.weight

        if self.origin.belongTo == "Face":
            properties["uv"] = self.uv

        return properties

    @property
    def weight(self):
        if self.origin.belongTo == "VertexGroup":
            if len(self.vertex.groups) == 0:
                raise TypeError("Vertex not assigned vertex groups.")

            vertexGroupIndex = self.origin.origin.vertex_groups.find(self.origin.accessor.name)
            if vertexGroupIndex < 0:
                return -1

            return self.vertex.groups[vertexGroupIndex].weight
        else:
            if len(self.vertex.groups) == 0:
                return []

            weights = []
            for vertexGroup in self.vertex.groups:
                vertexGroups = self.origin.origin.vertex_groups
                weights.append({ vertexGroups[vertexGroup.group].name: vertexGroup.weight })

            return weights

    @property
    def uv(self):
        if self.origin.belongTo != "Face":
            raise TypeError("Vertex is not belong Face.")

        uvs = {}
        for uvLayer in self.origin.origin.data.uv_layers:
             if len(uvLayer.data) > 0:
                uvs[uvLayer.name] = uvLayer.data[self.origin.accessor.toLoopIndex(self.index)].uv

        return uvs

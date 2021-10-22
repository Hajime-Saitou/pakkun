import bpy
from mathutils import Vector

class Vertex(bpy.types.MeshVertex):
    def __init__(self, vertex, origin):
        self.vertex = vertex
        self.origin = origin

    @property
    def serialize(self) -> dict:
        properties = {}
        properties["index"] = self.index
        properties["co"] = tuple(self.co)
        properties["hide"] = self.hide
        properties["normal"] = self.hide
        properties["select"] = self.select
        properties["undeformed_co"] = tuple(self.undeformed_co)

        if self.origin.belongTo == "VertexGroup":
            properties["weight"] = [ { self.origin.accessor.name: self.weight } ]
        else:
            properties["weight"] = self.weight

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
            for ordinal, vertexGroup in enumerate(self.origin.origin.vertex_groups):
                if ordinal in [ group.group for group in self.vertex.groups ]:
                    weights.append({ vertexGroup.name: self.vertex.groups[ordinal].weight })

            return weights

    @property
    def uv(self):
        if self.origin.belongTo != "Face":
            raise TypeError("Vertex is not belong Face.")

        uvs = {}
        for uvLayer in self.origin.origin.data.uv_layers:
            uvs[uvLayer.name] = uvLayer.data[self.origin.accessor.toLoopIndex(self.index)].uv

        return uvs

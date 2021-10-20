import bpy
from mathutils import Vector
import json

class Vertex(bpy.types.MeshVertex):
    def __init__(self, vertex, origin):
        self.vertex = vertex
        self.origin = origin

    def __str__(self):
        properties = {}
        properties["index"] = self.index
        properties["co"] = tuple(self.co)
        properties["hide"] = self.hide
        properties["normal"] = self.hide
        properties["select"] = self.select
        properties["undeformed_co"] = tuple(self.undeformed_co)

        if self.origin.belongTo == "VertexGroup":
            properties["weight"] = { self.origin.accessor.name: self.weight }
        else:
            properties["weight"] = self.weight

        return json.dumps(properties, indent=4)

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
            weights = {}
            for vertexGroup in self.origin.origin.vertex_groups:
                vertexGroupIndex = self.origin.origin.vertex_groups.find(vertexGroup.name)
                weights[vertexGroup.name] = self.groups[vertexGroupIndex].weight

            return weights

    @property
    def uv(self):
        if self.origin.belongTo != "Face":
            raise TypeError("Vertex is not belong Face.")

        uvs = {}
        for uvLayer in self.origin.origin.data.uv_layers:
            uvs[uvLayer.name] = uvLayer.data[self.origin.accessor.toLoopIndex(self.index)].uv

        return uvs
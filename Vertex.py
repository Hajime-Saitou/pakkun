import bpy

class Vertex(bpy.types.MeshVertex):
    def __init__(self, vertex, origin):
        self.vertex = vertex
        self.origin = origin

    @property
    def weight(self):
        if self.origin.belongTo != "VertexGroup":
            raise TypeError("Vertex is not belong VertexGroup.")

        if len(self.vertex.groups) == 0:
            raise TypeError("Vertex not assigned vertex groups.")

        vertexGroupIndex = self.origin.origin.vertex_groups.find(self.origin.accessor.name)
        if vertexGroupIndex < 0:
            return -1

        return self.vertex.groups[vertexGroupIndex].weight

    @property
    def uv(self):
        if self.origin.belongTo != "Face":
            raise TypeError("Vertex is not belong Face.")

        uvs = {}
        for uvLayer in self.origin.origin.data.uv_layers:
            uvs[uvLayer.name] = uvLayer.data[self.origin.accessor.toLoopIndex(self.index)].uv

        return uvs

import bpy
from mathutils import Vector
from .Origin import Origin
from .Vertices import Vertices

class VertexGroup(object):
    def __init__(self, vertexGroup, origin):
        self.vertexGroup = vertexGroup
        self.origin = origin

    @property
    def name(self) -> str:
        return self.vertexGroup.name

    @property
    def index(self) -> int:
        return self.vertexGroup.index

    @property        
    def vertices(self):
        vertices = [ vertex for vertex in self.origin.origin.data.vertices if self.index in [ group.group for group in vertex.groups ] ]
        return Vertices(vertices, Origin(self.origin.origin, self))

    def active(self):
        if self.origin.origin.mode != "EDIT":
            raise BlenderModeError("Blender mode must be set to 'EDIT'.")

        bpy.ops.object.vertex_group_set_active(group=self.name)

    def select(self):
        self.active()
        bpy.ops.object.vertex_group_select()

    def deselect(self):
        self.active()
        bpy.ops.object.vertex_group_deselect()

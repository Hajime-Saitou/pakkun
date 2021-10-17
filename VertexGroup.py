import bpy
from mathutils import Vector

class VertexGroup(object):
    def __init__(self, object, name:str):
        self.object = object
        self.name = name
        self.origin = Origin(self.object, self)

    @property
    def index(self):
        return self.object.vertex_groups.find(self.name)

    @property        
    def vertices(self):
        if self.index < 0:
            return None

        vertices = [ vertex for vertex in self.object.data.vertices if self.index in [ group.group for group in vertex.groups ] ]
        return Vertices(vertices, origin=self.origin)

    def active(self):
        if bpy.context.mode != "EDIT_MESH":
            bpy.ops.object.mode_set(mode="EDIT", toggle=False)

        bpy.ops.object.vertex_group_set_active(group=self.name)

    def select(self):
        self.active()
        bpy.ops.object.vertex_group_select()

    def deselect(self):
        self.active()
        bpy.ops.object.vertex_group_deselect()

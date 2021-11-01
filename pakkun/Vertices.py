import bpy
from mathutils import Vector
from .Vertex import Vertex
from .Origin import Origin
from .Iterator import Iterator
from .Exception.BlenderTypeError import BlenderTypeError

class Vertices(Iterator):
    def __init__(self, vertices, origin):
        super().__init__()

        self.vertices = vertices
        self._iterIndex = 0
        self.origin = origin

    def __getitem__(self, key):
        return Vertex(self.vertices[key], self.origin)

    @property
    def length(self) -> int:
        return len(self.vertices)

    @property
    def indeces(self) -> list:
        return [ vertex.index for vertex in self ]

    def __and__(self, other):
        vertices = [ vertex for vertex in self.vertices if vertex.index in list(set(self.indeces) & set(other.indeces)) ]
        return Vertices(vertices, Origin(self.origin.origin, self.__class__.__name__))

    def __or__(self, other):
        vertices = list(set(self.indeces + other.indeces))
        return Vertices(vertices, Origin(self.origin.origin, self.__class__.__name__))

    def __xor__(self, other):
        vertices = list(set(self.indeces) - set(other.indeces)) + list(set(other.indeces) - set(self.indeces))
        return Vertices(vertices, Origin(self.origin.origin, self.__class__.__name__))

    @property
    def serialize(self) -> dict:
        properties = {}
        properties["vertices"] = [ vertex.serialize for vertex in self ]
        return properties

    @property
    def gravity(self) -> Vector:
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.vertices[0].co

        summary = Vector(( 0, 0, 0 ))
        for vertex in self.vertices:
            summary += vertex.co

        return summary / self.length
    
    @property
    def dimension(self) -> Vector:
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.vertices[0].co

        minimum = Vector(( float("inf"), float("inf"), float("inf") ))
        maximum = Vector(( -float("inf"), -float("inf"), -float("inf") ))
        
        for vertex in self.vertices:
            minimum.x = min(minimum.x, vertex.co.x)
            minimum.y = min(minimum.y, vertex.co.y)
            minimum.z = min(minimum.z, vertex.co.z)

            maximum.x = max(maximum.x, vertex.co.x)
            maximum.y = max(maximum.y, vertex.co.y)
            maximum.z = max(maximum.z, vertex.co.z)

        return maximum - minimum

    def scale(self, scale:Vector, weighted:bool=False) -> None:
        if self.length == 0:
            return

        for vertex in self.vertices:
            v = Vertex(vertex, self.origin)
            weight = 1 if not weighted else v.weight
            vertex.co.x *= scale.x * weight
            vertex.co.y *= scale.y * weight
            vertex.co.z *= scale.z * weight

        self.origin.origin.data.update()

    def translate(self, translate:Vector, weighted:bool=False) -> None:
        if self.length == 0:
            return

        for vertex in self.vertices:
            v = Vertex(vertex, self.origin)
            weight = 1 if not weighted else v.weight
            v.co.x += translate.x * weight
            v.co.y += translate.y * weight
            v.co.z += translate.z * weight

        self.origin.origin.data.update()

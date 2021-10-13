
import bpy
from mathutils import Vector

class Vertices(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self._iterIndex = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._iterIndex < self.length:
            vertex = self.vertices[self._iterIndex]
            self._iterIndex += 1
            return vertex
        else:
            self._iterIndex = 0
            raise StopIteration()

    @property
    def length(self) -> int:
        return len(self.vertices)

    @property
    def gravity(self) -> Vector:
        if self.length == 0:
            return None

        summary = Vector(( 0, 0, 0 ))
        for vertex in self.vertices:
            summary += vertex.co

        return summary / self.length
    
    @property
    def dimension(self) -> Vector:
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

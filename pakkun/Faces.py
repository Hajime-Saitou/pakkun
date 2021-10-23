from .Face import Face

class Faces(object):
    def __init__(self, faces, origin):
        self.faces = faces
        self.origin = origin

    def __getitem__(self, key:int):
        return Face(self.faces[key])

    @property
    def length(self):
        return len(self.faces)

    def containingVertex(self, vertexIndex:int):
        faces = []
        for face in self.faces:
            if vertexIndex in face.vertices:
                faces.append(face)
        
        return Faces(faces, self.origin)

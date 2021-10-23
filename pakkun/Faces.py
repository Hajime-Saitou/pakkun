from .Face import Face

class Faces(object):
    def __init__(self, faces, origin):
        self.faces = faces
        self.origin = origin

    def __getitem__(self, key:int):
        return Face(self.origin.origin, key)

    @property
    def length(self):
        return len(self.faces)

    def __createSubset(self, faces):
        return None if len(faces) == 0 else Faces(faces, self.origin)

    def containingVertex(self, index:int):
        return self.__createSubset([ face for face in self.faces if index in face.vertices ])

    def containingMaterial(self, name:str):
        materialIndex:int = self.origin.origin.data.materials.find(name)
        if materialIndex == -1:
            raise KeyError(f"Undefined material name '{name}''.")

        return self.__createSubset([ face for face in self.faces if face.material_index == materialIndex ])

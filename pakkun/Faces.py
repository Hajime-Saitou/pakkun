from .Face import Face
from .Origin import Origin
from .Iterator import Iterator

class Faces(Iterator):
    def __init__(self, faces, origin):
        super().__init__()

        self.faces = faces
        self.origin = Origin(origin.origin, self)
        self._iterIndex:int = 0

    def __getitem__(self, key:int):
        if self.find(key) == -1:
            raise KeyError(f"Undefined face index '{key}'.")

        return Face(self.faces[key], self.origin)

    @property
    def length(self) -> int:
        return len(self.faces)

    def find(self, key) -> int:
        return if 0 <= key < self.length else -1

    def __createSubset(self, faces):
        return None if len(faces) == 0 else Faces(faces, self.origin)

    def containingVertex(self, index:int):
        return self.__createSubset([ face for face in self.faces if index in face.vertices ])

    def containingMaterial(self, name:str):
        materialIndex:int = self.origin.origin.data.materials.find(name)
        if materialIndex == -1:
            raise KeyError(f"Undefined material name '{name}''.")

        return self.__createSubset([ face for face in self.faces if face.material_index == materialIndex ])

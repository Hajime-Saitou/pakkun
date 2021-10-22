from .Face import Face

class Faces(object):
    def __init__(self, object):
        self.object = object

    def __getitem__(self, key):
        return Face(self.object, key)

    @property
    def length(self):
        return len(self.object.data.polygons)

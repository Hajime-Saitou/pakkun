class Iterator(object):
    def __init__(self):
        self.index:int = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < self.length:
            item = self.__getitem__(self.index)
            self.index += 1
            return item
        else:
            self.index = 0
            raise StopIteration()

    def __getitem__(self, key):
        raise NotImplementedError()

    @property
    def length(self):
        raise NotImplementedError()

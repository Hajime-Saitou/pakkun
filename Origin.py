class Origin(object):
    def __init__(self, origin, accessor):
        self.origin = origin
        self.accessor = accessor
        self.belongTo = accessor.__class__.__name__

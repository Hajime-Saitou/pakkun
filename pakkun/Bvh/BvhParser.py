import re

class StringTokenizer(object):
    def __init__(self):
        self.__data = None
        self.latestToken:str = ""
        self.generator = None

    @property
    def data(self) -> list:
        return self.__data

    @data.setter
    def data(self, data:str):
        self.__data = re.split(r"\s", data)
        self.generator = self.__generator

    @property
    def __generator(self) -> str:
        for token in self.data:
            if not token:
                continue
            yield token

    @property
    def next(self) -> str:
        token = self.generator.__next__()
        return token

class BvhChannels(object):
    def __init__(self, channels:tuple):
        self.size:int = channels[0]
        self.names:list = channels[1]

class BvhJoint(object):
    def __init__(self, name:str, offset:tuple, channels:tuple, parent:object):
        self.name:str = name
        self.offset:tuple = offset
        self.channels:BvhChannels = BvhChannels(channels)
        self.parent:object = parent
        self.childs:list = []
        if parent:
            parent.childs.append(self)

class BvhParser(object):
    def __init__(self):
        self.filename:str = ""
        self.loaded:bool = False
        self.tokenizer = StringTokenizer()
        self.joints:list = []

    def load(self, filename:str):
        with open(filename, "r") as f:
            self.tokenizer.data = f.read()

        self.loaded = True

    @property
    def data(self) -> list:
        return self.tokenizer.data

    @data.setter
    def data(self, data:str):
        self.tokenizer.data = data

    def parse(self):
        return self.hierarchy()

    def hierarchy(self):
        token = self.tokenizer.next
        if token != "HIERARCHY":
            raise ValueError("Invalid keyword in hierarchy.")

        self.root()

    def root(self):
        token = self.tokenizer.next
        if token != "ROOT":
            raise ValueError("Invalid keyword in root.")

        bonename = self.bonename()
        self.leftBrace()
        newJoint = BvhJoint(bonename, self.offset(), self.channels(), None)
        self.joints.append(newJoint)
        self.joint(newJoint)
        self.rightBrace()

    def leftBrace(self):
        token = self.tokenizer.next
        if token != "{":
            raise ValueError("Invalid left brace.")

    def rightBrace(self):
        token = self.tokenizer.next
        if token != "}":
            raise ValueError(f"Invalid right brace {token}.")

    def bonename(self):
        token = self.tokenizer.next
        if not re.match(r"[A-Za-z_]\w*", token):
            raise ValueError(f"Invalid bone name {token}.")
        
        return token

    def offset(self):
        token = self.tokenizer.next
        if token != "OFFSET":
            raise ValueError("Invalid keyword in offset.")

        offset = [ 0 ] * 3
        for index in range(len(offset)):
            token = self.tokenizer.next
            offset[index] = float(token)

        return tuple(offset)

    def channels(self):
        token = self.tokenizer.next
        if token != "CHANNELS":
            raise ValueError("Invalid keyword in channels.")

        token = self.tokenizer.next
        if token not in [ "3", "6" ]:
            raise ValueError("Invalid channel size.")
        channels:int = int(token)

        channelNames = [ "" ] * channels
        for index in range(channels):
            token = self.tokenizer.next
            if not re.match(r"[XYZ](position|rotation)", token):
                raise ValueError(f"Invalid channel name {token}.")

            channelNames[index] = token

        return ( channels, channelNames )

    def joint(self, parent:BvhJoint):
        token = self.tokenizer.next
        if token == "End":
            token = self.tokenizer.next
            if token == "Site":
                self.endsite(parent)
                return False

        if token == "}":
            return True

        if token != "JOINT":
            return False

        bonename = self.bonename()
        self.leftBrace()
        newJoint = BvhJoint(bonename, self.offset(), self.channels(), parent)
        self.joints.append(newJoint)

        while self.joint(newJoint):
            pass

        self.rightBrace()

        return True

    def endsite(self, parent:BvhJoint):
        self.leftBrace()
        self.joints.append(BvhJoint("End Site", self.offset(), ( None, None ), parent))
        self.rightBrace()

# class Bvh(object):

if __name__ == "__main__":
    filename:str = "C:\\temp\\cmuconvert-daz-01-09\\01\\01_01.bvh"
    parser = BvhParser()
    parser.load(filename)
    try:
        parser.parse()
    except:
        pass

    for joint in parser.joints:
        print(joint.name, joint.offset, joint.channels.size, joint.channels.names, joint.parent.name if joint.parent else "root")



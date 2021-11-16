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
        self.pushBacked:list = []

    @property
    def __generator(self) -> str:
        for token in self.data:
            if not token:
                continue
            yield token

    @property
    def next(self) -> str:
        if len(self.pushBacked):
            token = self.pushBacked.pop(0)
        else:
            token = self.generator.__next__()
        return token

    def pushBack(self, token:str):
        self.pushBacked.insert(0, token)

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

        self.keyFrames:list = []

class BvhMotion(object):
    def __init__(self):
        self.frames:int = 0
        self.frameTime:float = 0

class BvhParseResults(object):
    def __init__(self):
        self.joints:list = []
        self.motionInfo = BvhMotion()

class BvhParser(object):
    def __init__(self):
        self.filename:str = ""
        self.loaded:bool = False
        self.tokenizer = StringTokenizer()
        self.results = BvhParseResults()

    def load(self, filename:str):
        with open(filename, "r") as f:
            self.data = f.read()

        self.loaded = True

    @property
    def data(self) -> list:
        return self.tokenizer.data

    @data.setter
    def data(self, data:str):
        self.tokenizer.data = data

    def parse(self):
        self.hierarchy()
        self.motion()

        return self.results

    def hierarchy(self):
        token = self.tokenizer.next
        if token != "HIERARCHY":
            raise ValueError("Invalid keyword in hierarchy.")

        self.root()

    def root(self):
        token = self.tokenizer.next
        if token != "ROOT":
            raise ValueError("Invalid keyword in root.")

        boneName = self.boneName()
        self.leftBrace()
        newJoint = BvhJoint(boneName, self.offset(), self.channels(), None)
        self.results.joints.append(newJoint)
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

    def boneName(self):
        token = self.tokenizer.next
        if not re.match(r"[A-Za-z_]\w*", token):
            raise ValueError(f"Invalid bone name {token}.")

        boneName = token

        if boneName == "End":
            token = self.tokenizer.next
            if token != "Site":
                raise ValueError(f"Invalid bone name {token}.")
            boneName += token

        return boneName

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

    def joint(self, parentJoint:BvhJoint):
        token = self.tokenizer.next
        if token == "MOTION":
            self.tokenizer.pushBack(token)
            return
        elif token == "End":
            token = self.tokenizer.next
            if token != "Site":
                raise ValueError("Invalid end site.")
            self.endsite(parentJoint)
            return
        elif token != "JOINT":
            raise ValueError(f"Invalid keyword in joint {token}.")

        boneName = self.boneName()

        self.leftBrace()

        newJoint = BvhJoint(boneName, self.offset(), self.channels(), parentJoint)
        self.results.joints.append(newJoint)

        # search child joints
        while True:
            token = self.tokenizer.next
            self.tokenizer.pushBack(token)
            if token in [ "JOINT", "End" ]:
                self.joint(newJoint)
            else:
                break

        self.rightBrace()

        # serach brother joints
        while True:
            token = self.tokenizer.next
            self.tokenizer.pushBack(token)
            if token in [ "JOINT", "End" ]:
                self.joint(parentJoint)
            else:
                break

    def endsite(self, parentJoint:BvhJoint):
        self.leftBrace()
        newJoint = BvhJoint("End Site", self.offset(), ( 0, None ), parentJoint)
        self.results.joints.append(newJoint)
        self.rightBrace()

    def motion(self):
        token = self.tokenizer.next
        if token != "MOTION":
            raise ValueError("Invalid keyword in motion.")

        self.frames()
        self.frameTime()
        self.keyFrames()

    def frames(self):
        token = self.tokenizer.next
        if token != "Frames:":
            raise ValueError("Invalid keyword in frames.")

        self.results.motionInfo.frames = int(self.tokenizer.next)

    def frameTime(self):
        token = self.tokenizer.next
        if token != "Frame":
            raise ValueError("Invalid keyword in frame time.")

        token = self.tokenizer.next
        if token != "Time:":
            raise ValueError("Invalid keyword in frame time.")

        token = self.tokenizer.next
        self.results.motionInfo.frameTime = float(token)

    def keyFrames(self):
        for _ in range(self.results.motionInfo.frames):
            for joint in self.results.joints:
                channels = joint.channels.size
                if channels:
                    joint.keyFrames.append([ float(self.tokenizer.next) for _ in range(channels) ])

if __name__ == "__main__":
    filename:str = "C:\\temp\\cmuconvert-daz-01-09\\01\\01_01.bvh"
    parser = BvhParser()
    parser.load(filename)
    try:
        results = parser.parse()
    except ValueError as e:
        print(e)

    for joint in results.joints:
        print(joint.name, joint.offset, joint.channels.size, joint.channels.names, joint.parent.name if joint.parent else "root")



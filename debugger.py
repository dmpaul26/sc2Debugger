from string import lower
from replayImporter import ReplayImporter

class Debugger():

    def __init__(self):
        self.userCommand = ""

        self.getInput()
        self.handleInput()
        self.processReplay()

    def getInput(self):
        while self.userCommand != "load" and self.userCommand != "get":
            self.userCommand = raw_input("Load or get replay? ")

    def handleInput(self):
        replayImporter = ReplayImporter(self.userCommand)

        self.replay = replayImporter.replay

    def processReplay(self):
        print """

        {filename}
        --------------------------------------------
        SC2 Version {release_string}
        {category} Game, {start_time}
        {type} on {map_name}
        Length: {game_length}

        """.format(**self.replay.__dict__)

        print """
        Frames = {}, Frames/16 = {}
        replay.length.seconds = {}, replay.length.minutes = {}, self.replay.length.mins/1.4 = {}
        replay.real_length = {}
              """.format(self.replay.frames, self.replay.frames/16, self.replay.length.seconds,
                         self.replay.length.mins, self.replay.length.mins/1.4, self.replay.real_length.mins)

Debugger()
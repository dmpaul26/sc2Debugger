from urllib2 import Request, urlopen, URLError
import json, sc2reader

class ReplayImporter():

    def __init__(self, input):
        if input == "load":
            self.loadReplay()

        else:
            self.getReplay()

    def loadReplay(self):
        self.replay = sc2reader.load_replay("SC2Replay.SC2Replay")

    def getReplay(self):
        self.getUserID()
        try:
            url = Request('http://api.ggtracker.com/api/v1/matches?category=Ladder&game_type=1v1&identity_id=' + self.userID +
                          '&replay=true&filter=-graphs,match(replays,-map,-map_url),entity(-summary,-minutes,-armies)')

            page = urlopen(url)

            self.getRecentMatch(page)
        except URLError, e:
            print "Could not load player data, error: ", e

    def getUserID(self):
        self.userID = raw_input("Enter the GGTracker user ID: ")

    def updatePlayerInfo(self):
        for player in self.replay.players:
            if player.team is self.replay.teams[0]:
                self.parent.playerOneInfo.config(text=player.name)
            elif player.team is self.replay.teams[1]:
                self.parent.playerTwoInfo.config(text=player.name)

    def getRecentMatch(self, page): #processes the most recent 1v1 ranked match
        page_json = json.loads(page.read())

        replayURL = page_json['collection'][0]['replays'][0]['url']

        self.replay = sc2reader.load_replay(urlopen(Request(replayURL)))
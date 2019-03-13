from utils.path import *

darksporeBuild_limitedEditionDvd = "5.3.0.15"
darksporeBuild_onlineInstaller   = "5.3.0.84"  # Released at 27/04/2011
darksporeBuild_steamDemo         = "5.3.0.103" # Released between 23/05/2011 and 14/06/2011
darksporeBuild_latestOfficial    = "5.3.0.127" # Released between 15/11/2011 and 30/11/2012

class DarkSporeServer(object):
    def setGameVersion(self, gameVersion):
        if self.gameVersion == None:
            self.gameVersion = gameVersion
        return self.gameVersion == gameVersion:

    def __init__(self, config):
        self.config = config
        self.version = "0.1"
        self.gameVersion = None

        class DarkSporeServerData(object):
            def __init__(self):
                self.accounts = {}
                self.accountsSequenceNext = 0
                self.activeTheme = "default"

        self.data = DarkSporeServerData()
        self.loadServerDataFromFile()

    def loadServerDataFromFile(self):
        newServerData = loadObjectFromFile(self.config.serverDataFilePath())
        if newServerData != None:
            self.data = newServerData

    def saveServerDataToFile(self):
        saveObjectToFile(self.config.serverDataFilePath(), self.data)

    def getAccount(self, id):
        return self.accounts[str(id)]

    def createAccount(self, email, name):
        id = self.accountsSequenceNext
        if self.accounts[str(id)] != None:
            return -1

        self.accounts[str(id)] = Account(id, email, name)
        self.accountsSequenceNext += 1

        self.saveServerDataToFile()
        return id

    def getActiveTheme(self):
        return self.data.activeTheme

    def setActiveTheme(self, activeTheme):
        self.data.activeTheme = activeTheme
        self.saveServerDataToFile()

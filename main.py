class Entities:
    def __init__(self, activityStatus):
        self.activityStatus = activityStatus

    def isActive(self):
        if (self.activityStatus):
            return True
        else:
            return False

    def toggleActivity(self):
        if (self.activityStatus):
            self.activityStatus = False
        else:
            self.activityStatus = True


class Mario(Entities):
    def __init__(self, activityStatus):
        self.activityStatus = activityStatus

    def powerUp(self):
        print('You consumed the mushroom and gained a power up!')


class Mushroom(Entities):
    def __init__(self, activityStatus):
        self.activityStatus


class Tiles:
    def __init__(self, activityStatus):
        self.activityStatus = activityStatus

    def isActive(self):
        if (self.activityStatus):
            return True
        else:
            return False

    def toggleActivity(self):
        if (self.activityStatus):
            self.activityStatus = False
        else:
            self.activityStatus = True

    def onHit(self):
        pass


class BrickTile(Tiles):
    def __init__(self, activityStatus):
        self.activityStatus = activityStatus

    def onHit(self, brickNav):
        if (self.isActive):
            self.toggleActivity()
            brickNav.remove()
            print('You broke the brick tile!')


class QuestionCoinTile(Tiles):
    def __init__(self, activityStatus, hitTimes):
        self.activityStatus = activityStatus
        self.hitTimes = hitTimes

    def onHit(self):
        self.hitTimes -= 1
        if(self.hitTimes > 0):
            coins += 10
        else:
            self.toggleActivity()
            print('You have exhausted all hits to this tile!')


class QuestionMushroomTile(Tiles):
    def __init__(self, activityStatus):
        self.activityStatus = activityStatus
        self.hitTimes = 1

    def onHit(self, mushroom):
        self.hitTimes -= 1
        if(self.hitTimes > 0):
            mushroom.toggleActivity()
            print('A mushroom has been released!')
        else:
            print('You have exhausted all hits to this tile!')


class Portals:
    def gameExit(self):
        exit()


class Space:
    def __init__(self, xCord, yCord):
        self.xCord = xCord
        self.yCord = yCord

    def remove(self):
        self.xCord = -1
        self.yCord = -1

    def moveRight(self, portalNav):
        if (self.xCord + 1 != portalNav.xCord):
            self.xCord += 1
        else:
            print('Can\'t move coz of the tunnel!')

    def moveLeft(self):
        if(self.xCord - 1 != -1):
            self.xCord -= 1
        else:
            print('Cant move further left!')

    def moveUp(self, tileList):
        for i in range(len(tileList)):
            if (tileList[i].xCord == self.xCord and tileList[i].yCord == self.yCord + 1):
                tileList[i].onHit()
                break

    def moveDown(self, portalNav, portal):
        if (portalNav.xCord == self.xCord and portalNav.yCord + 1 == self.yCord):
            portal.gameExit()

    def moveUpLeft(self):
        self.moveLeft()

    def moveUpRight(self, portalNav):
        if (self.xCord + 1 == portalNav.xCord):
            self.xCord += 1
            self.yCord += 1
        else:
            self.moveRight()

coins = 0

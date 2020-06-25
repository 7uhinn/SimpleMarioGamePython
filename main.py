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
    def __init__(self, activityStatus, coins):
        self.activityStatus = activityStatus
        self.coins = coins

    def powerUp(self):
        print('\nYou consumed the mushroom and gained a power up!')


class Mushroom(Entities):
    def __init__(self, activityStatus):
        self.activityStatus = activityStatus


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
            print('\nYou broke the brick tile!')

class QuestionCoinTile(Tiles):
    def __init__(self, activityStatus, hitTimes):
        self.activityStatus = activityStatus
        self.hitTimes = hitTimes

    def onHit(self,mario):
        if(self.hitTimes > 0):
            mario.coins += 10
            print('\nCha Ching! 10 coins!')
        else:
            self.toggleActivity()
            print('\nYou have exhausted all hits to this tile!')
        self.hitTimes -= 1


class QuestionMushroomTile(Tiles):
    def __init__(self, activityStatus):
        self.activityStatus = activityStatus
        self.hitTimes = 1

    def onHit(self, mushroom):
        if(self.hitTimes > 0):
            mushroom.toggleActivity()
            print('\nA mushroom has been released!')
            self.toggleActivity()
        else:
            print('\nYou have exhausted all hits to this tile!')
        self.hitTimes -= 1


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
            print('\nCan\'t move coz of the tunnel!')

    def moveLeft(self):
        if(self.xCord - 1 != -1):
            self.xCord -= 1
        else:
            print('\nCant move further left!')

    def moveUp(self, tileList, mario, mushroom):
        for i in range(len(tileList)):
            if (tileList[i].xCord == self.xCord and tileList[i].yCord == self.yCord + 1):
                if(i == 0 or i == 2 or i == 4):
                    tileListObj[i].onHit(tileList[i])
                elif(i == 1):
                    tileListObj[i].onHit(mario)
                else:
                    tileListObj[i].onHit(mushroom)

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
            self.moveRight(portalNav)

# Location objects
marioNav = Space(0, 0)
portalNav = Space(12, 0)
brick1Nav = Space(4, 1)
brick2Nav = Space(6, 1)
brick3Nav = Space(8, 1)
quesCNav = Space(5, 1)
quesMNav = Space(7, 1)
mushroomNav = Space(7, 2)

# Actual Entity obejcts
mario = Mario(True,0)
mushroom = Mushroom(False)
brick1 = BrickTile(True)
brick2 = BrickTile(True)
brick3 = BrickTile(True)
portal = Portals()
quesC = QuestionCoinTile(True, 5)
quesM = QuestionMushroomTile(True)

f1 = 0
tileList = [brick1Nav, quesCNav, brick2Nav, quesMNav, brick3Nav]
tileListObj = [brick1, quesC, brick2, quesM, brick3]

print('----------------------------------------')
print('WELCOME TO SIMPLE MARIO GAME!')
print('----------------------------------------\n')

while (True):
    if (mushroom.isActive):
        locs = [[8, 1], [9, 0]]
        if (f1 < 2):
            mushroomNav.xCord = locs[f1][0]
            mushroomNav.yCord = locs[f1][1]
        f1 += 1

    if (mushroom.isActive and mushroomNav.xCord == marioNav.xCord and mushroomNav.yCord == marioNav.yCord):
        mushroom.toggleActivity()
        mushroomNav.remove()
        mario.powerUp()

    print('\n----------------------------------------')
    print('Your Surroundings and Coins:')
    print('----------------------------------------\n')

    if (marioNav.xCord == 4 or marioNav.xCord == 6 or marioNav.xCord == 8):
        if (tileListObj[marioNav.xCord - 4].isActive()):
            print('Up: There is a brick tile above you!')
        else:
            print('Up: Nothing.')
    elif (marioNav.xCord == 5 or marioNav.xCord == 7):
        if (tileListObj[marioNav.xCord - 4].isActive()):
            print('Up: there is a question mark tile above you!')
        else:
            print('Up: Static question mark tile.')
    else:
        print('Up: Nothing.')

    if (marioNav.xCord == portalNav.xCord - 1):
        print('Right: An exit tunnel!')
    elif(marioNav.xCord == mushroomNav.xCord - 1):
        print('Right: A power up mushroom!')
    else:
        print('Right: Nothing.')

    if(marioNav.xCord == mushroomNav.xCord + 1):
        print('Left: A power up mushroom!')
    else:
        print('Left: Nothing.')

    if(marioNav.xCord == portalNav.xCord and marioNav.yCord == portalNav.yCord + 1):
        print('Down: Exit!')
    else:
        print('Down: Nothing.\n')

    print('You have',mario.coins,'coins!\n')

    print('\n----------------------------------------')
    print('Choose your next move:')
    print('----------------------------------------\n')

    print('W: Jump')
    print('A: Left')
    print('D: Right')
    print('S: Down')
    print('E: Right Jump')
    print('Q: Left Jump\n')

    k = input('Your move key: ')

    if (k == 'w'):
        marioNav.moveUp(tileList,mario,mushroom)
    elif(k == 'a'):
        marioNav.moveLeft()
    elif(k == 'd'):
        marioNav.moveRight(portalNav)
    elif(k == 's'):
        marioNav.moveDown(portalNav,portal)
    elif(k == 'e'):
        marioNav.moveUpRight(portalNav)
    elif(k == 'q'):
        marioNav.moveUpLeft()
    else:
        print('Invalid!')

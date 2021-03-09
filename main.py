import random
from Players import Players
from DraftContainer import DraftContainer


draftRunning = 0
draftInstance = DraftContainer()
while draftRunning < 1:
    listOfPlayers = []
    draft = DraftContainer()
    for i in range(11):
        listOfPlayers.append(Players(i, None, False, False))
    while draftInstance.phaseNumber == 0:
        listOfPlayers[0].pickOrBan = True
        listOfPlayers[1].pickOrBan = True
        for i in range(3):
            listOfPlayers[0].champion = random.choice(draftInstance.champPool)
            draftInstance.champPool.remove(listOfPlayers[0].champion)
            listOfPlayers[1].champion = random.choice(draftInstance.champPool)
            draftInstance.champPool.remove(listOfPlayers[1].champion)

        draftInstance.phaseNumber = 1
    while draftInstance.phaseNumber == 1:
        listOfPlayers[0].pickOrBan = False
        listOfPlayers[0].champion = random.choice(draftInstance.champPool)
        draftInstance.champPool.remove(listOfPlayers[0].champion)
        draftInstance.phaseNumber = 2
    while draftInstance.phaseNumber == 2:
        listOfPlayers[1].pickOrBan = False
        listOfPlayers[3].pickOrBan = False
        listOfPlayers[1].champion = random.choice(draftInstance.champPool)
        draftInstance.champPool.remove(listOfPlayers[1].champion)
        listOfPlayers[3].champion = random.choice(draftInstance.champPool)
        draftInstance.champPool.remove(listOfPlayers[3].champion)
        draftInstance.phaseNumber = 3
    while draftInstance.phaseNumber == 3:
        listOfPlayers[2].pickOrBan = False
        listOfPlayers[3].pickOrBan = False
        listOfPlayers[2].champion = random.choice(draftInstance.champPool)
        draftInstance.champPool.remove(listOfPlayers[2].champion)
        listOfPlayers[4].champion = random.choice(draftInstance.champPool)
        draftInstance.champPool.remove(listOfPlayers[4].champion)
        draftInstance.phaseNumber = 4
    while draftInstance.phaseNumber == 4:
        listOfPlayers[5].pickOrBan = False
        listOfPlayers[5].champion = random.choice(draftInstance.champPool)
        draftInstance.champPool.remove(listOfPlayers[5].champion)
        listOfPlayers[1].pickOrBan = True
        listOfPlayers[0].pickOrBan = True
        for i in range(2):
            listOfPlayers[0].champion = random.choice(draftInstance.champPool)
            draftInstance.champPool.remove(listOfPlayers[0].champion)
            listOfPlayers[1].champion = random.choice(draftInstance.champPool)
            draftInstance.champPool.remove(listOfPlayers[1].champion)
        listOfPlayers[7].champion = random.choice(draftInstance.champPool)
        draftInstance.champPool.remove(listOfPlayers[7].champion)
        draftInstance.phaseNumber = 5
    while draftInstance.phaseNumber == 5:
        listOfPlayers[6].pickOrBan = False
        listOfPlayers[8].pickOrBan = False
        listOfPlayers[6].champion = random.choice(draftInstance.champPool)
        draftInstance.champPool.remove(listOfPlayers[6].champion)
        listOfPlayers[8].champion = random.choice(draftInstance.champPool)
        draftInstance.champPool.remove(listOfPlayers[8].champion)
        draftInstance.phaseNumber = 6
    while draftInstance.phaseNumber == 6:
        listOfPlayers[9].pickOrBan = False
        listOfPlayers[9].champion = random.choice(draftInstance.champPool)
        draftInstance.champPool.remove(listOfPlayers[9].champion)
        draftInstance.phaseNumber = 7

    draftRunning = 1
for i in range(10):
    print(vars(listOfPlayers[i]))
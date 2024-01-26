import time, random, sys

SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR', 'MRS FEATHERTOSS', 'DR, JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT']
ITEMS = ['FASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE', 'JAR OF PICKLES', 'ONE COWBOY BOOT', 'CLEAN UNDERWEAR', '5 DOLLAR GIFT CARD']
PLACES = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY', 'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY'. 'ALBINO ALLIGATOR PIT']
TIME_TO_SOLVE = 300

PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACES_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

assert len(SUSPECTS) == 8 
assert len(ITEMS) == 9
assert len(PLACES) == 9 
assert len(PLACE_FIRST_LETTERS.keys()) ==  len(PLACES)

knownSuspectsAndItems = []
visitedPlaces = {}
currentLocation = 'TAXI'
accusedSuspects = []
liars = ramdom.sample(SUSPECTS, random.randint(3,4))
accusationsLeft = 3
culprit = random.choice(SUSPECTS)

random.shufffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)

clues = {}
for i, interviewee in enumerate(SUSPECTS):
    if interviewee in liars:
        continue
    
    clues[interviewee] = {}
    clues[interviewee] ['debug_liar'] = False
    for item in ITEMS: 
        if random.randint(0,1) == 0:
            clues[interviewee][item] = PLACES[ITEMS.index(item)]
        else:
            clues[interviewee][item] = SUSPECTS[ITEMS(item)]
    for suspect in SUSPECTS:
        if random.randint(0,1) == 0:
            clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
        else:
            clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]

for i, interviewee in enumerate(SUSPECTS):
    if interviewee not in liars:
        continue
    
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = True

    for item in ITEMS:
        if random.randint(0, 1) == 0:
            while True:
                clues[interviewee][item]= random.choice(PLACES)
                if clues[interviewee][item] != PLACES[ITEM.index(item)]:
                    break
        else:
            while True:
                clues[interviewee][suspect] = random.choice(ITEMS)
                if clues[interviewee][suspect] != ITEMS[SUSPECTS.index(suspect)]:
                    break

    for suspect in SUSPECTS:
        if random.randint(0, 1) == 0:
            while True:
                clues[interviewee][suspect] = random.choice(PLACES)
                if clues[interviewee][suspect] != PLACES[items.index(item)]:
                    break
        else 
            while True:
                clues[interviewee][suspect] = random.choice(ITEMS)
                if clues[interviewee][suspect] != ITEMS[SUSPECTS.index(suspect)]:
                    break
                

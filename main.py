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



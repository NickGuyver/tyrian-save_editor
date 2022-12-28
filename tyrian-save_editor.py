import PySimpleGUI as sg

from binascii import *
from ctypes import *
from struct import *
from sys import *

from collections import OrderedDict

# Define all the upgrades
frontWeapon = 0
rearWeapon = 1
leftSidekick = 3
rightSidekick = 4
generator = 5
shield = 9
special = 10
ship = 11

# Set all the items as available
allAvailable = [
    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, # Front/Rear Weapons 1-38 
	0,0,0,0,0,0,0,0,0,0,1,                                                           # Fill                    
	1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,                                             # Sidekicks          51-68
	0,0,0,0,0,0,0,0,0,0,0,                                                           # Fill                    
	1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,                                                   # Special Weapons    81-93
	0,0,0,0,0,                                                                      
    0,0,0,0]

# Used for storing the lists of items
shipList = []
frontList = []
rearList = []
shieldList = []
generatorList = []
sidekickList = []
specialList = []

# Used for looking up values, and generating the lists
# Front Weapon
frontWeapons = OrderedDict()
frontWeapons['Pulse-Cannon'] = b'\x01'
frontWeapons['Multi-Cannon'] = b'\x02'
frontWeapons['Mega Cannon'] = b'\x03'
frontWeapons['Laser'] = b'\x04'
frontWeapons['Zica Laser'] = b'\x05'
frontWeapons['Protron Z'] = b'\x06'
frontWeapons['Vulcan Cannon'] = b'\x07'
frontWeapons['Lightning Cannon'] = b'\x08'
frontWeapons['Protron'] = b'\x0C'
frontWeapons['Miscellaneous Option Weapons'] = b'\x10'
frontWeapons['Missile Launcher'] = b'\x11'
frontWeapons['Mega Pulse'] = b'\x13'
frontWeapons['Heavy Missile Launcher'] = b'\x14'
frontWeapons['Banana Blast'] = b'\x17'
frontWeapons['HotDog Front'] = b'\x19'
frontWeapons['Hyper Pulse'] = b'\x1B'
frontWeapons['Guided Bombs'] = b'\x1F'
frontWeapons['Shuruiken Field'] = b'\x20'
frontWeapons['Poison Bomb'] = b'\x21'
frontWeapons['Protron Wave'] = b'\x22'
frontWeapons['The Orange Juicer'] = b'\x23'
frontWeapons['NortShip Super Pulse'] = b'\x24'
frontWeapons['Atomic RailGun'] = b'\x27'
frontWeapons['Widget Beam'] = b'\x28'
frontWeapons['Sonic Impulse'] = b'\x29'
frontWeapons['RetroBall'] = b'\x30'
frontWeapons['None'] = b'\x31'

# Rear Weapon
rearWeapons = OrderedDict()
rearWeapons['Starburst'] = b'\x09'
rearWeapons['Multi-Cannon'] = b'\x0A'
rearWeapons['Sonic Wave'] = b'\x0B'
rearWeapons['Protron'] = b'\x0D'
rearWeapons['Wild Ball'] = b'\x0E'
rearWeapons['Vulcan Cannon'] = b'\x0F'
rearWeapons['Fireball'] = b'\x12'
rearWeapons['Rear Heavy Missile Launcher'] = b'\x15'
rearWeapons['Rear Mega Pulse'] = b'\x16'
rearWeapons['Banana Blast Rear'] = b'\x18'
rearWeapons['HotDog Rear'] = b'\x1A'
rearWeapons['Guided Micro Bombs'] = b'\x1C'
rearWeapons['Heavy Guided Bombs'] = b'\x1D'
rearWeapons['Scatter Wave'] = b'\x1E'
rearWeapons['NortShip Spreader'] = b'\x25'
rearWeapons['NortShip Spreader B'] = b'\x26'
rearWeapons['None'] = b'\x31'

# Sidekick
sidekicks = OrderedDict()
sidekicks['Single Shot Option'] = b'\x01'
sidekicks['Dual Shot Option'] = b'\x02'
sidekicks['Charge Cannon'] = b'\x03'
sidekicks['Vulcan Shot Option'] = b'\x04'
sidekicks['Wobbley'] = b'\x05'
sidekicks['MegaMissile'] = b'\x06'
sidekicks['Atom Bombs'] = b'\x07'
sidekicks['Phoenix Device'] = b'\x08'
sidekicks['Plasma Storm'] = b'\x09'
sidekicks['Mini-Missile'] = b'\x0A'
sidekicks['Buster Rocket'] = b'\x0B'
sidekicks['Zica SuperCharger'] = b'\x0C'
sidekicks['MicroBomb'] = b'\x0D'
sidekicks['8-Way MicroBomb'] = b'\x0E'
sidekicks['Post-It Mine'] = b'\x0F'
sidekicks['Mint-O-Ship'] = b'\x10'
sidekicks['Zica Flamethrower'] = b'\x11'
sidekicks['Side Ship'] = b'\x12'
sidekicks['Companion Ship Warfly'] = b'\x13'
sidekicks['MicroSol FrontBlaster'] = b'\x14'
sidekicks['Companion Ship Gerund'] = b'\x15'
sidekicks['BattleShip-Class Firebomb'] = b'\x16'
sidekicks['Protron Cannon Indigo'] = b'\x17'
sidekicks['Companion Ship Quicksilver'] = b'\x18'
sidekicks['Protron Cannon Tangerine'] = b'\x19'
sidekicks['MicroSol FrontBlaster II'] = b'\x1A'
sidekicks['Beno Wallop Beam'] = b'\x1B'
sidekicks['Beno Protron System -B-'] = b'\x1C'
sidekicks['Tropical Cherry Companion'] = b'\x1D'
sidekicks['Satellite Marlo'] = b'\x1E'

# Generator
generators = OrderedDict()
generators['Standard MR-9'] = b'\x01'
generators['Advanced MR-12'] = b'\x02'
generators['Gencore Custom MR-12'] = b'\x03'
generators['Standard MicroFusion'] = b'\x04'
generators['Advanced MircoFusion'] = b'\x05'
generators['Gravitron Pulse-Wave'] = b'\x06'
generators['None'] = b'\x07'

# Shields
shields = OrderedDict()
shields['Structural Integrity Field'] = b'\x01'
shields['Advanced Integrity Field'] = b'\x02'
shields['Gencore Low Energy Shield'] = b'\x03'
shields['Gencore High Energy Shield'] = b'\x04'
shields['MicroCorp LXS Class A'] = b'\x05'
shields['MicroCorp LXS Class B'] = b'\x06'
shields['MicroCorp LXS Class C'] = b'\x07'
shields['MicroCorp HXS Class A'] = b'\x08'
shields['MicroCorp HXS Class B'] = b'\x09'
# This is not normally available and glitches the interface
shields['MicroCorp HXS Class C'] = b'\x0a'

# Special
specials = OrderedDict()
specials['Repulsor'] = b'\x01'
specials['Pearl Wind'] = b'\x02'
specials['Soul of Zinglon'] = b'\x03'
specials['Attractor'] = b'\x04'
specials['Ice Beam'] = b'\x05'
specials['Flare'] = b'\x06'
# There are more "specials" but they don't work correctly when assigned through saves
#specials['Blade Field'] = b'\x07'
#specials['SandStorm'] = b'\x08'
#specials['MineField'] = b'\x09'
#specials['Dual Vulcan'] = b'\x0A'
#specials['Banana Bomb'] = b'\x0B'
#specials['Protron Dispersal'] = b'\x0C'
#specials['Astral Zone'] = b'\x0D'
#specials['Xega Ball'] = b'\x0E'
#specials['MegaLaser Dual'] = b'\x0F'
#specials['Orange Shield'] = b'\x10'
#specials['Pulse Blast'] = b'\x11'
#specials['MegaLaser'] = b'\x12'

# Ships
ships = OrderedDict()
ships['USP Talon Light Fighter'] = b'\x01'
ships['SuperCarrot'] = b'\x02'
ships['Gencore Phoenix'] = b'\x03'
ships['Gencore Maelstrom'] = b'\x04'
ships['MicroCorp Stalker'] = b'\x05'
ships['MicroCorp Stalker-B'] = b'\x06'
ships['Prototype Stalker-C'] = b'\x07'
ships['Stalker'] = b'\x08'
ships['USP Fang Light Fighter'] = b'\x09'
ships['U-Ship'] = b'\x0A'
ships['Silver Ship'] = b'\x0B'
ships['Nort Ship'] = b'\x0C'
ships['The Stalker 21.126'] = b'\x0D'
ships['None'] = b'\x0E'

# Pulled from OpenTyrian source
cryptKey = [15, 50, 89, 240, 147, 34, 86, 9, 32, 208]
SAVE_FILES_SIZE = 2398
SIZEOF_SAVEGAMETEMP = SAVE_FILES_SIZE + 4 + 100
SAVE_FILE_SIZE = (SIZEOF_SAVEGAMETEMP - 4)

# All the different fields within a single save
class saveFiles:
    encode = []
    level = []
    items = []    
    #[0]  = items->weapon[FRONT_WEAPON].id; https://tyrian.fandom.com/wiki/Front_Guns
	#[1]  = items->weapon[REAR_WEAPON].id; https://tyrian.fandom.com/wiki/Rear_Guns
	#[2]  = items->super_arcade_mode;
	#[3]  = items->sidekick[LEFT_SIDEKICK]; https://tyrian.fandom.com/wiki/Sidekicks
	#[4]  = items->sidekick[RIGHT_SIDEKICK]; https://tyrian.fandom.com/wiki/Sidekicks
	#[5]  = items->generator; https://tyrian.fandom.com/wiki/Generators
	#[6]  = items->sidekick_level;
	#[7]  = items->sidekick_series;
	#[8]  = initial_episode_num;
	#[9]  = items->shield; https://tyrian.fandom.com/wiki/Shields
	#[10] = items->special; https://tyrian.fandom.com/wiki/Special_Weapons
	#[11] = items->ship; https://tyrian.fandom.com/wiki/Ships
    score = []
    #saveFiles[slot-1].score  = player[0].cash;
    score2 = []
    levelName = []
    name = []
    cubes = []
    power = []
    #power[0] - front weapon level
    #power{1] - rear weapon level
    episode = []
    lastItems = []
    difficulty = []
    secretHint = []
    input1 = []
    input2 = []
    gameHasRepeated = []
    initialDifficulty = []
    highScore1 = []
    highScore2 = []
    highScoreName = []
    highScoreDiff = []


# Check to see if the save is decryptable
def decryptionTest(saveTemp, s2):
    y = 0
    for x in range(0, SAVE_FILE_SIZE, 1):
        y += s2[x]
        
    if saveTemp[SAVE_FILE_SIZE] != (y % 256):
        correct = False
        decryptionError = (f'Failed additive checksum: {saveTemp[SAVE_FILE_SIZE]} vs {y}\n')
        
    y = 0
    for x in range(0, SAVE_FILE_SIZE, 1):
        y -= s2[x]
        
    if saveTemp[SAVE_FILE_SIZE+1] != (y % 256):
        correct = False
        decryptionError = (f'Failed subtractive checksum: {saveTemp[SAVE_FILE_SIZE+1]} vs {y}\n')
        
    y = 1
    for x in range(0, SAVE_FILE_SIZE, 1):
        y = (y * s2[x]) + 1
        
    if saveTemp[SAVE_FILE_SIZE+2] != (y % 256):
        correct = False
        decryptionError = (f'Failed multiplicative checksum: {saveTemp[SAVE_FILE_SIZE+2]} vs {y}\n')
        
    y = 0
    for x in range(0, SAVE_FILE_SIZE, 1):
        y ^= s2[x];
    
    if saveTemp[SAVE_FILE_SIZE+3] != (y % 256):
        correct = False
        decryptionError = (f'Failed XOR checksum: {saveTemp[SAVE_FILE_SIZE+3]} vs {y}\n')
        
    return True, 0


# Decrypt the selected save file
def JE_decryptSaveTemp(saveTemp):
    import inspect
    
    correct = True
    decryptionError = ''
    s2 = [0] * SIZEOF_SAVEGAMETEMP
    x = 0
    y = 0
    
    for x in range((SAVE_FILE_SIZE - 1), 0, -1):
        s2[x] = saveTemp[x] ^ cryptKey[(x+1) % 10]
        
        if x > 0:
            s2[x] = s2[x] ^ saveTemp[x - 1]
    
    correct, decryptionError = decryptionTest(saveTemp, s2)
    
    if inspect.stack()[1].function == 'JE_loadConfiguration':
        if not correct:
            window['decryptStatus'].update(decryptionError)
            return 0
        
        else:
            window['decryptStatus'].update('Successfully Decrypted')
        
        return s2
    
    else:
        if not correct:
            window['encryptStatus'].update(decryptionError)
        
        else:
            window['encryptStatus'].update('Successfully Encrypted')
    

# Encrypt the selected save file
def JE_encryptSaveTemp(saveTemp):
    s3 = saveTemp
    x = 0
    y = 0
        
    y = 0
    for x in range(0, SAVE_FILE_SIZE, 1):
        y += s3[x]
        
    saveTemp[SAVE_FILE_SIZE] = (y % 256)
        
    y = 0
    for x in range(0, SAVE_FILE_SIZE, 1):
        y -= s3[x]
        
    saveTemp[SAVE_FILE_SIZE+1] = (y % 256)
        
    y = 1
    for x in range(0, SAVE_FILE_SIZE, 1):
        y = (y * s3[x]) + 1
        
    saveTemp[SAVE_FILE_SIZE+2] = (y % 256)
        
    y = 0
    for x in range(0, SAVE_FILE_SIZE, 1):
        y ^= s3[x]
    
    saveTemp[SAVE_FILE_SIZE+3] = (y % 256)
        
    for x in range(0, SAVE_FILE_SIZE, 1):
        saveTemp[x] = saveTemp[x] ^ cryptKey[(x+1) % 10]
        
        if x > 0:
            saveTemp[x] = saveTemp[x] ^ saveTemp[x - 1]
    
    return saveTemp
    

# Opens, decrypts, and loads the selected save file
def JE_loadConfiguration(inFile):
    availableItems = []
    
    saveFiles.encode = []
    saveFiles.level = []
    saveFiles.items = []
    saveFiles.score = []
    saveFiles.score2 = []
    saveFiles.levelName = []
    saveFiles.name = []
    saveFiles.cubes = []
    saveFiles.power = []
    saveFiles.episode = []
    saveFiles.lastItems = []
    saveFiles.difficulty = []
    saveFiles.secretHint = []
    saveFiles.input1 = []
    saveFiles.input2 = []
    saveFiles.gameHasRepeated = []
    saveFiles.initialDifficulty = []
    saveFiles.highScore1 = []
    saveFiles.highScore2 = []
    saveFiles.highScoreName = []
    saveFiles.highScoreDiff = []
    
    byteList = []
    p = 0
    saveRead = []
    
    with open(inFile, 'rb') as tyrianSav:        
        for i in range(0, SIZEOF_SAVEGAMETEMP, 1):
            fileRead = tyrianSav.read(1)
            saveRead.append(int.from_bytes(fileRead, "little"))
            
    decryptedSav = JE_decryptSaveTemp(saveRead)
    
    if not decryptedSav:
        return 0
    
    for i in bytes(decryptedSav):
        byteList.append(i.to_bytes(1, byteorder="big"))
    
    # This is all pulled from OpenTyrian source
    for z in range(0, 22, 1):
        saveItems = []
        saveLevelName = []
        saveName = []
        saveLastItems = []
        saveHighScoreName = []
        
        saveFiles.encode.append([byteList[p], byteList[p+1]])
        p += 2
        
        saveFiles.level.append([byteList[p], byteList[p+1]])
        p += 2
        
        for i in range(0, 12, 1):
            saveItems.append(byteList[p+i])
        saveFiles.items.append(saveItems)
        p += 12
        
        saveFiles.score.append([byteList[p], byteList[p+1], byteList[p+2], byteList[p+3]])
        p += 4
        
        saveFiles.score2.append([byteList[p], byteList[p+1], byteList[p+2], byteList[p+3]])
        p += 4
        
        for i in range(0, 10, 1):
            saveLevelName.append(byteList[p+i])
        saveFiles.levelName.append(saveLevelName)
        p += 10
        
        for i in range(0, 14, 1):
            saveName.append(byteList[p+i])
        saveFiles.name.append(saveName)
        p += 14
        
        saveFiles.cubes.append(byteList[p])
        p += 1
        
        saveFiles.power.append([byteList[p], byteList[p+1]])
        p += 2
        
        saveFiles.episode.append(byteList[p])
        p += 1
        
        for i in range(0, 12, 1):
            saveLastItems.append(byteList[p+i])
        saveFiles.lastItems.append(saveLastItems)
        p += 12
        
        saveFiles.difficulty.append(byteList[p])
        p += 1
        
        saveFiles.secretHint.append(byteList[p])
        p += 1
        
        saveFiles.input1.append(byteList[p])
        p += 1
        
        saveFiles.input2.append(byteList[p])
        p += 1
        
        saveFiles.gameHasRepeated.append(byteList[p])
        p += 1
        
        saveFiles.initialDifficulty.append(byteList[p])
        p += 1
        
        saveFiles.highScore1.append([byteList[p], byteList[p+1], byteList[p+2], byteList[p+3]])
        p += 4
        
        saveFiles.highScore2.append([byteList[p], byteList[p+1], byteList[p+2], byteList[p+3]])
        p += 4
        
        for i in range(0, 30, 1):
            saveHighScoreName.append(byteList[p+i])
        saveFiles.highScoreName.append(saveHighScoreName)
        p += 30
        
        saveFiles.highScoreDiff.append(byteList[p])
        p += 1
    
    for i in range(0, 104, 1):
        availableItems.append(int.from_bytes(byteList[p+i], 'little'))
        
    editorLevel = decryptedSav[SIZEOF_SAVEGAMETEMP - 5] << 8 | decryptedSav[SIZEOF_SAVEGAMETEMP - 6]
    
    return editorLevel
    

# Encrypts, and saves the selected file, ready to load into the game
def JE_saveConfiguration(outFile):
    modifiedSav = []
    p = 0
    
    for z in range(0, 22, 1):
        saveItems = []
        saveScore = []
        saveScore2 = []
        saveLevelName = []
        saveName = []
        saveLastItems = []
        saveHighScore1 = []
        saveHighScore2 = []
        saveHighScoreName = []
        
        modifiedSav.append(int.from_bytes(saveFiles.encode[z][0], "big"))
        modifiedSav.append(int.from_bytes(saveFiles.encode[z][1], "big"))
        p += 2
        
        modifiedSav.append(int.from_bytes(saveFiles.level[z][0], "big"))
        modifiedSav.append(int.from_bytes(saveFiles.level[z][1], "big"))
        p += 2
        
        for i in range(0, 12, 1):
            saveItems.append(int.from_bytes(saveFiles.items[z][i], "big"))
        modifiedSav.extend(saveItems)
        p += 12
        
        for i in range(0, 4, 1):
            saveScore.append(int.from_bytes(saveFiles.score[z][i], "big"))
        modifiedSav.extend(saveScore)
        p += 4
        
        for i in range(0, 4, 1):
            saveScore2.append(int.from_bytes(saveFiles.score2[z][i], "big"))
        modifiedSav.extend(saveScore2)
        p += 4
        
        for i in range(0, 10, 1):
            saveLevelName.append(int.from_bytes(saveFiles.levelName[z][i], "big"))
        modifiedSav.extend(saveLevelName)
        p += 10
        
        for i in range(0, 14, 1):
            saveName.append(int.from_bytes(saveFiles.name[z][i], "big"))
        modifiedSav.extend(saveName)
        p += 14
        
        modifiedSav.append(int.from_bytes(saveFiles.cubes[z], "big"))
        p += 1
        
        modifiedSav.append(int.from_bytes(saveFiles.power[z][0], "big"))
        modifiedSav.append(int.from_bytes(saveFiles.power[z][1], "big"))
        p += 2
        
        modifiedSav.append(int.from_bytes(saveFiles.episode[z], "big"))
        p += 1
        
        for i in range(0, 12, 1):
            saveLastItems.append(int.from_bytes(saveFiles.lastItems[z][i], "big"))
        modifiedSav.extend(saveLastItems)
        p += 12
        
        modifiedSav.append(int.from_bytes(saveFiles.difficulty[z], "big"))
        p += 1
        
        modifiedSav.append(int.from_bytes(saveFiles.secretHint[z], "big"))
        p += 1
        
        modifiedSav.append(int.from_bytes(saveFiles.input1[z], "big"))
        p += 1
        
        modifiedSav.append(int.from_bytes(saveFiles.input2[z], "big"))
        p += 1
        
        modifiedSav.append(int.from_bytes(saveFiles.gameHasRepeated[z], "big"))
        p += 1
        
        modifiedSav.append(int.from_bytes(saveFiles.initialDifficulty[z], "big"))
        p += 1
        
        for i in range(0, 4, 1):
            saveHighScore1.append(int.from_bytes(saveFiles.highScore1[z][i], "big"))
        modifiedSav.extend(saveHighScore1)
        p += 4
        
        for i in range(0, 4, 1):
            saveHighScore2.append(int.from_bytes(saveFiles.highScore2[z][i], "big"))
        modifiedSav.extend(saveHighScore2)
        p += 4
        
        for i in range(0, 30, 1):
            saveHighScoreName.append(int.from_bytes(saveFiles.highScoreName[z][i], "big"))
        modifiedSav.extend(saveHighScoreName)
        p += 30
        
        modifiedSav.append(int.from_bytes(saveFiles.highScoreDiff[z], "big"))
        p += 1
    
    # Might adjust this in the future to only make selected items available
    modifiedSav.extend(allAvailable)
        
    modifiedSav[SIZEOF_SAVEGAMETEMP - 5] = editorLevel >> 8
    modifiedSav[SIZEOF_SAVEGAMETEMP - 6] = (editorLevel % 256)
    
    encryptedSav = JE_encryptSaveTemp(modifiedSav)

    with open(outFile, 'wb') as tyrianOut:
        tyrianOut.write(bytearray(encryptedSav))
        
    # Check to make sure the encryption was successful
    saveRead = []
    
    with open(outFile, 'rb') as tyrianSav:        
        for i in range(0, SIZEOF_SAVEGAMETEMP, 1):
            fileRead = tyrianSav.read(1)
            saveRead.append(int.from_bytes(fileRead, "little"))
    
    decryptedSav = JE_decryptSaveTemp(saveRead)
    
    if not decryptedSav:
        return 0


# All of the item lookup functions are to return the byte value of the selected name
def shipLookup(shipValue):
    for name, value in ships.items():
        if value == shipValue:
            return name


def frontweaponLookup(weaponValue):
    for name, value in frontWeapons.items():
        if value == weaponValue:
            return name
            
            
def rearweaponLookup(weaponValue):
    for name, value in rearWeapons.items():
        if value == weaponValue:
            return name
            

def shieldLookup(shieldValue):
    for name, value in shields.items():
        if value == shieldValue:
            return name


def generatorLookup(generatorValue):
    for name, value in generators.items():
        if value == generatorValue:
            return name
            
            
def sidekickLookup(sidekickValue):
    for name, value in sidekicks.items():
        if value == sidekickValue:
            return name
            
            
def specialLookup(specialValue):
    for name, value in specials.items():
        if value == specialValue:
            return name


# Create all the item lists based on the items in the OrderedDicts
def generateLists():
    for item in ships.items():
        shipList.append(item[0])
        
    for item in frontWeapons.items():
        frontList.append(item[0])
    
    for item in rearWeapons.items():
        rearList.append(item[0])
    
    for item in shields.items():
        shieldList.append(item[0])
    
    for item in generators.items():
        generatorList.append(item[0])
    
    for item in sidekicks.items():
        sidekickList.append(item[0])
        
    for item in specials.items():
        specialList.append(item[0])
    
    
def generatesaveList():
    saveList = []
    
    for item in saveFiles.name:
        saveList.append(b''.join(item).decode())
    
    saveList = saveList[:11]
    
    return saveList


# Main function below
generateLists()

# Create the main GUI window and it's elements
levelList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

column_one = [[sg.Text('Load tyrian.sav')],
              [sg.Input(), sg.FileBrowse(key='-IN-')],
              [sg.Button('Decrypt'), sg.Text(key='decryptStatus')],
              [sg.Text()],
              [sg.Text('Select Save Slot')],
              [sg.Combo([], key='saveCombo', enable_events=True, size=16)],
              [sg.Text()],
              [sg.Text('Create Save')],
              [sg.Input(key='outField'), sg.FileBrowse(key='-OUT-')],
              [sg.Button('Encrypt'), sg.Button('Exit'), sg.Text(key='encryptStatus')]]
              
column_two = [[sg.Text('Current Loadout')],
            [sg.Text('Ship\t\t'), sg.Combo(values=shipList, key='shipCombo', enable_events=True)],
            [sg.Text('Front Gun\t'), sg.Spin(values=(levelList), initial_value='', key='frontLevel', enable_events=True), sg.Combo(values=frontList, key='frontCombo', enable_events=True)],
            [sg.Text('Rear Gun\t\t'), sg.Spin(values=(levelList), initial_value='', key='rearLevel', enable_events=True), sg.Combo(values=rearList, key='rearCombo', enable_events=True)],
            [sg.Text('Shield\t\t'), sg.Combo(values=shieldList, key='shieldCombo', enable_events=True)],
            [sg.Text('Generator\t'), sg.Combo(values=generatorList, key='generatorCombo', enable_events=True)],
            [sg.Text('Left Sidekick\t'), sg.Combo(values=sidekickList, key='leftCombo', enable_events=True)],
            [sg.Text('Right Sidekick\t'), sg.Combo(values=sidekickList, key='rightCombo', enable_events=True)],
            [sg.Text('Special\t\t'), sg.Combo(values=specialList, key='specialCombo', enable_events=True)],]
              
layout = [[sg.Column(column_one),
            sg.VSeperator(),
            sg.Column(column_two)]]

window = sg.Window('Tyrian Save Editor', layout)
        
while True:
    event, values = window.read()
    inFile = values['-IN-']
    outFile = f'{values["-IN-"]}.out'
    
    if event == 'Decrypt':
        editorLevel = 0
        
        # Clear out the item and save values when decrypting a new file
        window['saveCombo'].update(values=[])
        window['shipCombo'].update(value='')
        window['frontLevel'].update(value='')
        window['frontCombo'].update(value='')
        window['rearLevel'].update(value='')
        window['rearCombo'].update(value='')
        window['shieldCombo'].update(value='')
        window['generatorCombo'].update(value='')
        window['leftCombo'].update(value='')
        window['rightCombo'].update(value='')
        window['specialCombo'].update(value='')
        window['outField'].update(outFile)
        
        editorLevel = JE_loadConfiguration(inFile)
        
        # Only load the save if the editorLevel correctly pulled
        if editorLevel:
            saveNames = generatesaveList()
            window['saveCombo'].update(values=saveNames)
    
    elif event == 'saveCombo':
        saveSelection = saveNames.index((values['saveCombo']))
        
        # Clear out item values when a new save slot is selected
        window['shipCombo'].update(value='')
        window['frontLevel'].update(value='')
        window['frontCombo'].update(value='')
        window['rearLevel'].update(value='')
        window['rearCombo'].update(value='')
        window['shieldCombo'].update(value='')
        window['generatorCombo'].update(value='')
        window['leftCombo'].update(value='')
        window['rightCombo'].update(value='')
        window['specialCombo'].update(value='')
        
        window['shipCombo'].update(value=shipLookup(saveFiles.items[saveSelection][ship]))
        window['frontLevel'].update(value=int.from_bytes(saveFiles.power[saveSelection][0], "little"))
        window['frontCombo'].update(value=frontweaponLookup(saveFiles.items[saveSelection][frontWeapon]))
        window['rearLevel'].update(value=int.from_bytes(saveFiles.power[saveSelection][1], "little"))
        window['rearCombo'].update(value=rearweaponLookup(saveFiles.items[saveSelection][rearWeapon]))
        window['shieldCombo'].update(value=shieldLookup(saveFiles.items[saveSelection][shield]))
        window['generatorCombo'].update(value=generatorLookup(saveFiles.items[saveSelection][generator]))
        window['leftCombo'].update(value=sidekickLookup(saveFiles.items[saveSelection][leftSidekick]))
        window['rightCombo'].update(value=sidekickLookup(saveFiles.items[saveSelection][rightSidekick]))
        window['specialCombo'].update(value=specialLookup(saveFiles.items[saveSelection][special]))
    
    # Update the class when a new item is selected
    elif event == 'shipCombo':
        saveFiles.items[saveSelection][ship] = ships[values['shipCombo']]
    
    elif event == 'frontLevel':
        saveFiles.power[saveSelection][0] = values['frontLevel'].to_bytes(1, byteorder="big")
        
    elif event == 'frontCombo':
        saveFiles.items[saveSelection][frontWeapon] = frontWeapons[values['frontCombo']]
        
    elif event == 'rearLevel':
        saveFiles.power[saveSelection][1] = values['rearLevel'].to_bytes(1, byteorder="big")
        
    elif event == 'rearCombo':
        saveFiles.items[saveSelection][rearWeapon] = rearWeapons[values['rearCombo']]
    
    elif event == 'shieldCombo':
        saveFiles.items[saveSelection][shield] = shields[values['shieldCombo']]
    
    elif event == 'generatorCombo':
        saveFiles.items[saveSelection][generator] = generators[values['generatorCombo']]
    
    elif event == 'leftCombo':
        saveFiles.items[saveSelection][leftSidekick] = sidekicks[values['leftCombo']]
    
    elif event == 'rightCombo':
        saveFiles.items[saveSelection][rightSidekick] = sidekicks[values['rightCombo']]
        
    elif event == 'specialCombo':
        saveFiles.items[saveSelection][special] = specials[values['specialCombo']]
        
    elif event == 'Encrypt' and editorLevel:
        JE_saveConfiguration(outFile)
    
    elif event == sg.WIN_CLOSED or event == 'Exit':
        break
import random
import mingus.core.notes as notes
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.midi import fluidsynth

# Checks if two lists of notes are exactly equal. (Order of the notes matter.)
def noteLists_AreExactEqual(list1, list2):

    if(len(list1) != len(list2)):
        return False
        
    areEqual = True    
    for x in range(len(list1)):
        if(not notes.is_enharmonic(list1[x], list2[x])):
            areEqual = False
    
    return areEqual


def init_FluidSynth():
    fluidsynth.init("soundfonts/FluidR3_GM.sf2") # Here you can put the path of whichever soundfont you would like to use.

# Asks a question.
def melody_Quiz(roundNumber, numNotes, numOctaves, bpm):
    print("Round " + str(roundNumber))
    print("Name each note in the melody (separated by spaces) or type \"R\" to hear it again.")

    # Calculate range of possible notes from numOctaves.
    lowNote = (4 - (numOctaves // 2)) * 12
    highNote = (4 + ((numOctaves - 1) // 2)) * 12 + 11

    # Randomly select each note in the melody.
    randomMelody = Bar('C', (numNotes, 4))
    for x in range(numNotes):
        n = Note().from_int(random.randint(lowNote, highNote))        
        randomMelody.place_notes(n, 4)
    
    response = "" # The player's answer.
    playAgain = True # Does the player want to hear the melody again?

    while(playAgain):
        fluidsynth.play_Bar(randomMelody, 1, bpm) # Play the melody.

        response = input().split() # Get the player's answer.

        invalidResponse = True # If the player's response is invalid.
        while(response != ["R"] and invalidResponse):            
            invalidResponse = False
            # Check if each note is valid.
            for x in response:
                if(not notes.is_valid_note(x)):
                    invalidResponse = True

            if(invalidResponse):                
                print("Invalid response. Try again.")
                response = input().split()

        if(response != ["R"]):
            playAgain = False         

    randomMelody_noteList = []
    for x in range(numNotes):
        randomMelody_noteList.append(randomMelody[x][2][0].name) #lol

    answeredCorrectly = noteLists_AreExactEqual(response, randomMelody_noteList)

    melodyName = ""
    for x in randomMelody_noteList:
        if(melodyName == ""):
            melodyName = melodyName + x
        else:
            melodyName = melodyName + " " + x

    if(answeredCorrectly):
        print("Correct. The melody was " + melodyName + ". Type \"R\" to hear the melody again or press enter to continue.")
    else:
        print("Incorrect. The melody was " + melodyName + ". Type \"R\" to hear the melody again or press enter to continue.")    
    
    playAgainResponse = input()
    playAgain = (playAgainResponse == "R")

    while(playAgain):
        fluidsynth.play_Bar(randomMelody, 1, bpm)
        print("Type \"R\" to hear the melody again or press enter to continue.")
        playAgainResponse = input()
        playAgain = (playAgainResponse == "R")
    

# The main script.
init_FluidSynth()

print("--- Melody Training ---")

goAgain = True # Does the player want to play again?

while(goAgain):
    print("How many rounds?")
    numRounds = int(input())

    print("How many notes in each melody? (integer between 2 and 8)")
    numNotes = int(input())

    print("How many octaves should the notes be chosen from? (integer between 1 and 7)")
    numOctaves = int(input())

    print("How many beats per minute? (integer roughly between 100 and 400)")
    bpm = int(input())

    print()
    for x in range(numRounds):
        melody_Quiz(x + 1, numNotes, numOctaves, bpm)

    print("Go again? Type \"Y\" or \"N\".")
    response = input()
    goAgain = (response == "Y")
    if(goAgain):
        print()

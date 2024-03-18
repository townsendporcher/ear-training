import random
import mingus.core.notes as notes
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.midi import fluidsynth

# Checks if lists of notes are equal up to permutation of the notes.
def noteLists_AreEqual(list1, list2):

    if(len(list1) != len(list2)):
        return False
    
    list1_copy = list1.copy()
    list2_copy = list2.copy()
    
    areEqual = True    
    for x in list1_copy:
        isMatch = False
        matchIndex = -1
        for y in list2_copy:
            if(notes.is_enharmonic(x, y)):
                isMatch = True
                matchIndex = list2_copy.index(y)
        if(isMatch):            
            list2_copy.pop(matchIndex)
        else:
            areEqual = False
    
    return areEqual


def init_FluidSynth():
    fluidsynth.init("soundfonts/FluidR3_GM.sf2") # Here you can put the path of whichever soundfont you would like to use.

# Asks a question.
def harmony_Quiz(roundNumber, numNotes, numOctaves):
    print("Round " + str(roundNumber))
    print("Name each note in the chord (separated by spaces) or type \"R\" to hear it again.")

    # Calculate range of possible notes from numOctaves.
    lowNote = (4 - (numOctaves // 2)) * 12
    highNote = (4 + ((numOctaves - 1) // 2)) * 12 + 11

    # Sample numNotes random notes in the specified range.
    listOfNotes = random.sample(range(lowNote, highNote + 1), numNotes)
    randomChord = NoteContainer()
    for x in range(numNotes):
        n = Note().from_int(listOfNotes[x])
        randomChord.add_note(n)
    
    response = "" # The player's answer.
    playAgain = True # Does the player want to hear the chord again?

    while(playAgain):
        fluidsynth.play_NoteContainer(randomChord) # Play the chord.

        response = input().split() # Get the player's answer.

        invalidResponse = True # If the player's response is invalid.
        while(response != ["R"] and invalidResponse):            
            invalidResponse = False
            for x in response:
                if(not notes.is_valid_note(x)):
                    invalidResponse = True

            if(invalidResponse):                
                print("Invalid response. Try again.")
                response = input().split()

        if(response != ["R"]):
            playAgain = False         

    randomChord_noteList = []
    for x in range(numNotes):
        randomChord_noteList.append(randomChord[x].name)

    answeredCorrectly = noteLists_AreEqual(response, randomChord_noteList)

    chordName = ""
    for x in randomChord_noteList:
        if(chordName == ""):
            chordName = chordName + x
        else:
            chordName = chordName + " " + x

    if(answeredCorrectly):
        print("Correct. The chord was " + chordName + ". Type \"R\" to hear the chord again or press enter to continue.")
    else:
        print("Incorrect. The chord was " + chordName + ". Type \"R\" to hear the chord again or press enter to continue.")    
    
    playAgainResponse = input()
    playAgain = (playAgainResponse == "R")

    while(playAgain):
        fluidsynth.play_NoteContainer(randomChord)
        print("Type \"R\" to hear the chord again or press enter to continue.")
        playAgainResponse = input()
        playAgain = (playAgainResponse == "R")
    

# The main script.
init_FluidSynth()
print("--- Harmony Training ---")

goAgain = True # Does the player want to play again?

while(goAgain):
    print("How many rounds?")
    numRounds = int(input())

    print("How many notes in each chord? (integer from 2 to 8)")
    numNotes = int(input())

    print("How many octaves should the notes be chosen from? (integer from 1 to 7)")
    numOctaves = int(input())

    print()
    for x in range(numRounds):
        harmony_Quiz(x + 1, numNotes, numOctaves)

    print("Go again? Type \"Y\" or \"N\".")
    response = input()
    goAgain = (response == "Y")
    if(goAgain):
        print()
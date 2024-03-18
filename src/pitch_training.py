import random
import mingus.core.notes as notes
from mingus.containers import Note
from mingus.midi import fluidsynth

def init_FluidSynth():
    fluidsynth.init("soundfonts/FluidR3_GM.sf2") # Here you can put the path of whichever soundfont you would like to use.

# Asks a question.
def pitch_Quiz(roundNumber):
    print("Round " + str(roundNumber))
    print("Name the note or type \"R\" to hear it again.")

    # Generates a random note on the piano from C1 to B7.
    randomPitchInt = random.randint(12, 95)
    randomPitch = Note().from_int(randomPitchInt)

    response = "" # The player's answer.
    playAgain = True # Does the player want to hear the note again?

    while(playAgain):
        fluidsynth.play_Note(randomPitch) # Play the note.

        response = input() # Get the player's answer.

        while(not(response == "R" or notes.is_valid_note(response))): # If the response is invalid.
            print("Invalid response. Try again.")
            response = input()

        if(response != "R"):
            playAgain = False         

    answeredCorrectly = notes.is_enharmonic(response, randomPitch.name)

    if(answeredCorrectly):
        print("Correct. Type \"R\" to hear the note again or press enter to continue.")
    else:
        print("Incorrect. The note was " + randomPitch.name + ". Type \"R\" to hear the note again or press enter to continue.")    
    
    playAgainResponse = input()
    playAgain = (playAgainResponse == "R")

    while(playAgain):
        fluidsynth.play_Note(randomPitch)
        print("Type \"R\" to hear the note again or press enter to continue.")
        playAgainResponse = input()
        playAgain = (playAgainResponse == "R")
    

# The main script.
init_FluidSynth()
print("--- Pitch Training ---")

goAgain = True # Does the player want to play again?

while(goAgain):
    print("How many rounds?")
    numRounds = int(input())

    print()
    for x in range(numRounds):
        pitch_Quiz(x + 1)

    print("Go again? Type \"Y\" or \"N\".")
    response = input()
    goAgain = (response == "Y")
    if(goAgain):
        print()
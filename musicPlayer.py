
"""
Simple music player style app that can play a standard mp3 audio file
***MUST install the pygame package by running: pip install pygame

"""
from pygame import mixer

# initialize the mixer
mixer.init()

print("\nWelcome to the Python Music Player")
print("Press 1 to select a song file")
print("Press 2 to play the chosen song")
print("Press 3 to pause song")
print("Press 4 to unpause song")
print("Press any other key to exit program")

while True:
	menuChoice = input("Enter a menu option >>")

	if menuChoice == "1":
		songFile = input("Enter the song filename >>")
		# load that music file into the mixer
		mixer.music.load(songFile)
		continue
	elif menuChoice == "2":
		# play the loaded music file
		mixer.music.play()
		continue
	elif menuChoice == "3":
	    # pause current song
	    mixer.music.pause()
	    continue	
	elif menuChoice == "4":
		# take song out of pause mode
		mixer.music.unpause()
		continue
	else:
		break
# final sign-off message when the user quits and the loop is done
print("Existing music player...")

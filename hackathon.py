import random
from gtts import gTTS  # Text-to-speech library
import os

# Game parameters
number_range = 10
font_size = "20px"  # Increase font size for better readability

# Generate a random number
secret_number = random.randint(1, number_range)

# Start the game loop
guesses = 0
while True:
  # Get user input (modify for alternative input methods)
  guess = int(input("Guess a number between 1 and {}: ".format(number_range)))

  # Track guesses
  guesses += 1

  # Check the guess
  if guess == secret_number:
    # Text-to-speech feedback
    speech = gTTS(text="Congratulations! You guessed the number in {} tries.".format(guesses))
    speech.save("success.mp3")
    os.system("mpg321 success.mp3")  # Play the audio file (adjust for different systems)
    
    print("Congratulations! You guessed the number in {} tries.".format(guesses), style=f"font-size: {font_size}")  # Increase font size
    break  # Exit the loop on correct guess
  elif guess < secret_number:
    # Text-to-speech feedback
    speech = gTTS(text="Too low, try again!")
    speech.save("too_low.mp3")
    os.system("mpg321 too_low.mp3")

    print("Too low, try again!", style=f"font-size: {font_size}")
  else:
    # Text-to-speech feedback
    speech = gTTS(text="Too high, try again!")
    speech.save("too_high.mp3")
    os.system("mpg321 too_high.mp3")

    print("Too high, try again!", style=f"font-size: {font_size}")

# End of game message (consider adding visual cues)
print("The secret number was:", secret_number, style=f"font-size: {font_size}")
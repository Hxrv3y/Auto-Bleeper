import speech_recognition as sr
import winsound

# Set up the recognizer
r = sr.Recognizer()
mic = sr.Microphone()

# Set up the list of bad words
bad_words = ["Swear word here", ["Naughty words"], ["More if you want"]]
#good_words = ["Good words here"]

# Main loop
while True:
    # Listen for speech
    print("Listening...")
    with mic as source:
        audio = r.listen(source)

    # Try to recognize the speech
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")

        # Check for bad words
        for word in bad_words:
            if word in text.lower():
                # Play a bleep sound
                winsound.PlaySound("bleep.wav", winsound.SND_FILENAME)
                break
                
       #for word in good_words:
           # if word in text.lower():
                # Play good word sound
                #winsound.PlaySound("AudioFileHere.wav", winsound.SND_FILENAME)
              #  break

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error recognizing speech: {e}")

import speech_recognition as sr

def transcribe_voice():
    # Initialize the recognizer class
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for background noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Microphone is ready. Speak now...")

        try:
            # Listen to the audio input from the user
            audio_data = recognizer.listen(source, timeout=5)
            print("Processing audio...")

            # Transcribe audio using Google's free web API
            text = recognizer.recognize_google(audio_data)
            print(f"Transcription: {text}")

        except sr.WaitTimeoutError:
            print("Error: No speech detected within the timeout period.")
        except sr.UnknownValueError:
            print("Error: Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Error: Could not request results from the service; {e}")

if __name__ == "__main__":
    transcribe_voice()
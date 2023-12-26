import speech_recognition as sr
from pydub import AudioSegment

# Convert MP3 to WAV (required for speech_recognition)
sound = AudioSegment.from_mp3("your_audio_file.mp3")
sound.export("audio.wav", format="wav")

# Transcribe audio using Google Speech Recognition
r = sr.Recognizer()
with sr.AudioFile("audio.wav") as source:
    audio = r.record(source)  # Read the entire audio file

try:
    transcription = r.recognize_google(audio)  # Use Google Speech Recognition
    print("Transcription:", transcription)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(
            e
        )
    )

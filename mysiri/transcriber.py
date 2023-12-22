import pyaudio
import wave
import speech_recognition as sr
import subprocess

from commands import Commander

running = True


def say(text):
    subprocess.call("say " + text, shell=True)


def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, "rb")
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True,
    )

    data_stream = wf.readframes(chunk)
    while data_stream:

        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


# '''
# file = pyglet.resource.media('audio/ohyeah.wav')
# file.play()
# pyglet.app.run()
# '''

r = sr.Recognizer()
cmd = Commander()


def initSpeech():
    print("Listening....")
    # play_audio("./audio/okay.wav")
    say("sh!")
    with sr.Microphone() as source:
        print("Say Something ...")
        audio = r.listen(source)

    # play_audio("./audio/yes.wav")
    say("Done!")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Could not understand you, bro")

    print(command)

    if command in ["quit", "exit", "shutdown", "goodbye", "bye"]:
        global running
        running = False

    cmd.discover(command)


while running == True:
    initSpeech()

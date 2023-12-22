import pyaudio
import wave
import speech_recognition as sr
import logging as logger


def play_audio(filename):
    logger.info(f"\tProcessing audio: {filename}")
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
    logger.info("Closing stream.  Ready to terminate process.")
    pa.terminate()


# '''
# file = pyglet.resource.media('audio/ohyeah.wav')
# file.play()
# pyglet.app.run()
# '''

r = sr.Recognizer()


def initSpeech():
    print("Listening....")
    play_audio("./audio/okay.wav")
    with sr.Microphone() as source:
        print("Say Something ...")
        audio = r.listen(source)

    play_audio("./audio/yes.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except Exception as e:
        logger.error("Could not complete command: ", e)

    print("Your command")
    print(command)


initSpeech()

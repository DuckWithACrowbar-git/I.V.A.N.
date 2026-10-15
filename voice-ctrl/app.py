from vosk import Model, KaldiRecognizer
import pyaudio
import os, sys
from pathlib import Path

MODEL_PATH = "model"
os.chdir(Path(__file__).resolve().parent)

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()

stream = p.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 16000,
    input = True,
    frames_per_buffer = 8000
)
stream.start_stream()

try:
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            print(recognizer.Result())
        else:
            print(recognizer.PartialResult())

except KeyboardInterrupt:
    print("\n Exiting!")
    sys.exit(0)

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
from pathlib import Path

import speech_recognition as sr

r = sr.Recognizer()
call_file = sr.AudioFile(str(Path("C:\\") / "git" / "ham2mon-recognize" / "test" / "wav" / "147.260_1611618513_norm.wav"))
with call_file as source:
    audio = r.record(source)
resp = r.recognize_google(audio)

print(resp)

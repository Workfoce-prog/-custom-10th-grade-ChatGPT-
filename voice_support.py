
import pyttsx3
import base64

def text_to_audio_base64(text, filename="voice.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    with open(filename, "rb") as f:
        audio_bytes = f.read()
        encoded = base64.b64encode(audio_bytes).decode()
    return encoded

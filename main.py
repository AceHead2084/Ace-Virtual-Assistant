import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("How can I help you?")
    audio = r.listen(source)

try:
    print("Ace believes you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Ace could not understand you :(")
except sr.RequestError as e:
    print("Ace had a problem; {0}".format(e))
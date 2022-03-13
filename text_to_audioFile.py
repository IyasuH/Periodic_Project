from comtypes.client import CreateObject
# file I used to creat audio file
engine = CreateObject("SAPI.SpVoice")
stream = CreateObject("SAPI.SpFileStream")
from comtypes.gen import SpeechLib
# Enter text separetly to create audio file
# After you run this script it will create audio files with the text given as name on this folder
text = ["Elements with 1 Valance Electrons", "Elements with 2 Valance Electrons", "Elements with 3 Valance Electrons", "Elements with 4 Valance Electrons", "Elements with 5 Valance Electrons", "Elements with 6 Valance Electrons", "Elements with 7 Valance Electrons", "Elements with 8 Valance Electrons"]
for i in text:
    outfile = ("{}.mp3".format(i))
    stream.Open(outfile, SpeechLib.SSFMCreateForWrite)
    engine.AudioOutputStream = stream
    theText = i
    engine.speak(theText)
    stream.Close()

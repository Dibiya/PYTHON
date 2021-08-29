from gtts import gTTS
import os
myText = "Hi shanmuga dev i love u"
language = 'en'
output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")
os.system(" output.mp3")
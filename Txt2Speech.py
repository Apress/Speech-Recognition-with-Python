from gtts import gTTS
import os
text1="Welcome to the course"
language='en'
obj=gTTS(text=text1, lang=language, slow=False)
obj.save("welcome.mp3")
os.system("welcome.mp3")
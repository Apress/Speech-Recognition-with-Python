import speech_recognition as srg
import pyttsx3

r = srg.Recognizer()
# recognizer

# function to convert speech to txt

def Speech(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while(1):

    try:

        with srg.Microphone() as source1:
            r.adjust_for_ambient_noise(source1,duration=0.2)
            audio1=r.listen(source1)

            MyText=r.recognize_google(audio1)
            MyText=MyText.lower()

            print("Did you say ", MyText)
            Speech(MyText)

    except srg.RequestError as e:
        print("cant request results; {0}".format(e))

    except srg.UnknownValueError:
        print("unknown error")



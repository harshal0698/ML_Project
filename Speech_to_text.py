import speech_recognition as sr    
 
r = sr.Recognizer()                
a = int(input("Press 1 to give input as audio file or Press 2 to use Microphone"))
if(a == 1):
        AUDIO_FILE=input("Enter the file name:")
        with sr.AudioFile(AUDIO_FILE) as source:
                audio = r.record(source)
                try:	 
                        print("The audio file contains"+r.recognize_google(audio))
                except:
                        print("Sorry Could not understand audio")
else:
        with sr.Microphone() as source:     
                print("Speak Anything :")
                audio = r.listen(source)        
                try:
                        text1 = r.recognize_google(audio)    
                        print("You said : {}".format(text1))
                except:
                        print("Sorry could not recognize your voice")   

from Speech_Drive_Dependencies import pyttsx3

destiny_engine = pyttsx3.init()
destiny_voice = destiny_engine.getProperty('voices')
destiny_engine.setProperty('voice', destiny_voice[2].id)
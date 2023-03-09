from Destiny_Speech_Drive import DSD
import time, sys, datetime, os, random, Destiny_TTS_Input_Text



def anim_print(str):                                                            
    print(str,end="")
    sys.stdout.flush()


def initial_text():                                                            
    anim_print(Destiny_TTS_Input_Text.destiny_engine_initialize_text)
    
    
def initial_speech():                                                          
    DSD.destiny_engine.say(Destiny_TTS_Input_Text.destiny_engine_initialize_text)
    

def greet_by_time_text():                                                      
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        anim_print(Destiny_TTS_Input_Text.greet_by_time_text1)

    elif hour>=12 and hour<16:
        anim_print(Destiny_TTS_Input_Text.greet_by_time_text2)  

    else:
        anim_print(Destiny_TTS_Input_Text.greet_by_time_text3)


def greet_by_time_speech():                                                    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        DSD.destiny_engine.say(Destiny_TTS_Input_Text.greet_by_time_text1)

    elif hour>=12 and hour<16:
        DSD.destiny_engine.say(Destiny_TTS_Input_Text.greet_by_time_text2)   

    else:
        DSD.destiny_engine.say(Destiny_TTS_Input_Text.greet_by_time_text3)      


def user_custom_text_ask():                                                    
    anim_print(Destiny_TTS_Input_Text.ask_dailougue)
    
    
def user_custom_speech_ask():                                                  
    DSD.destiny_engine.say(Destiny_TTS_Input_Text.ask_dailougue)


def play_music():                                                              
    music_dir = 'D:\\OS\\User Data\\Music\\'
    songs = os.listdir(music_dir)
    length = len(songs)
    random_element = random.randrange(length)
    os.startfile(os.path.join(music_dir, songs[random_element]))

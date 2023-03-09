from Destiny_Speech_Drive import DSD
import Destiny_Protocols, datetime, sys, Destiny_update_db, Destiny_Threader
                                                                
custom_text = sys.argv[1].lower()
resp =  ['Yes, Boss!','I Have Choosen, A Random Song For You. Enjoy!','For U Boss! Always.','Sure. See You Later.','Sorry, Iam Under Development. Currently, This Far Is Only I Can Do. Thankyou.']

if 'honey' in custom_text:

      Destiny_update_db.update('honey',resp[0])
      DSD.destiny_engine.say(str(resp[0]))
      DSD.destiny_engine.runAndWait() 
      
elif 'play music' in custom_text:

      Destiny_update_db.update('play music',resp[1])      
      DSD.destiny_engine.say(str(resp[1]))
      DSD.destiny_engine.runAndWait() 
      Destiny_Protocols.play_music()

elif 'thank you' in custom_text:

      Destiny_update_db.update('thank you',resp[2])      
      DSD.destiny_engine.say(str(resp[2]))
      DSD.destiny_engine.runAndWait()
      #break
            
elif 'the time' in custom_text:
      strTime = datetime.datetime.now().strftime("%H:%M:%S")   
      Destiny_update_db.update('the time', strTime) 
      DSD.destiny_engine.say(f"the time is {strTime}")
      DSD.destiny_engine.runAndWait()
      
            
elif 'bye' in custom_text:

      Destiny_update_db.update('bye',resp[3])
      DSD.destiny_engine.say(str(resp[3]))
      DSD.destiny_engine.runAndWait()
      #break

else:
      
      Destiny_update_db.update('undefined input',resp[4])
      DSD.destiny_engine.say(str(resp[4]))
      DSD.destiny_engine.runAndWait()
      



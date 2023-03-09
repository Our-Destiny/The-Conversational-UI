import Destiny_Threader, Destiny_Protocols
import sqlite3 as sqlite

def createDb():
    conn = sqlite.connect('./GUI/js/returnResp.sqlite')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS response')
    cur.execute('CREATE TABLE response (id INT, input TEXT, output TEXT) ')
    cur.execute('DELETE from response where id = 1')
    conn.close()


initial_thread = Destiny_Threader.Destiny_Threading_Process(Destiny_Protocols.initial_speech, Destiny_Protocols.initial_text)
greet_by_time_thread = Destiny_Threader.Destiny_Threading_Process(Destiny_Protocols.greet_by_time_speech, Destiny_Protocols.greet_by_time_text)
custom_input_speak = Destiny_Threader.Destiny_Threading_Process(Destiny_Protocols.user_custom_speech_ask, Destiny_Protocols.user_custom_text_ask)


initial_thread.destiny_thread()
greet_by_time_thread.destiny_thread()
custom_input_speak.destiny_thread()

createDb()

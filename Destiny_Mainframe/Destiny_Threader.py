import threading
from Destiny_Speech_Drive import DSD


class Destiny_Threading_Process:

    
    def __init__ (self, destiny_text_to_print, destiny_text_to_speak):
        self.destiny_print = destiny_text_to_print
        self.destiny_speech = destiny_text_to_speak

    
    def destiny_thread(self):
        t1 = threading.Thread(target=self.destiny_speech, daemon=True)
        t2 = threading.Thread(target=self.destiny_print, daemon=True)
        t2.start()
        t1.start()
        DSD.destiny_engine.runAndWait()
        t1.join()
        t2.join()

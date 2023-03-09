'''DESTINY Autonimous Artificial Intelligence Programme (Python 3).
Copyright (c) 2012 - End Of Times | OUR DESTINY (A.A.I) Research And Development Labs,Inc.
All rights reserved. This software or any portion thereof may not be reproduced or used in any manner whatsoever without the development permission of the ODRE Labs, Inc.
Permission for the development of the software is Authorized ONLY for the developers of ODRD Labs, Inc.
Author: OUR DESTINY (A.A.I) Research And Development Labs <hariprasad@ODRDLabs>|<ribin@ODRDLabs>'''

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

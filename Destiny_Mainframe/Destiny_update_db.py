'''DESTINY Autonimous Artificial Intelligence Programme (Python 3).
Copyright (c) 2012 - End Of Times | OUR DESTINY (A.A.I) Research And Development Labs,Inc.
All rights reserved. This software or any portion thereof may not be reproduced or used in any manner whatsoever without the development permission of the ODRE Labs, Inc.
Permission for the development of the software is Authorized ONLY for the developers of ODRD Labs, Inc.
Author: OUR DESTINY (A.A.I) Research And Development Labs <hariprasad@ODRDLabs>|<ribin@ODRDLabs>'''

import sqlite3 as sqlite

def update(in1,out1):
    conn = sqlite.connect('./GUI/js/returnResp.sqlite')
    cur = conn.cursor()
    cur.execute('DELETE from response where id = 1')
    cur.execute('INSERT INTO response (id, input, output) VALUES (?,?,?)', (1, str(in1) , str(out1)))
    conn.commit()
    conn.close()

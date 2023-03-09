import sqlite3 as sqlite
def update(in1,out1):
    conn = sqlite.connect('./GUI/js/returnResp.sqlite')
    cur = conn.cursor()
    cur.execute('DELETE from response where id = 1')
    cur.execute('INSERT INTO response (id, input, output) VALUES (?,?,?)', (1, str(in1) , str(out1)))
    conn.commit()
    conn.close()

# db 접속

import sqlite3


def getconn():
    conn = sqlite3.connect("c:/pydb/webdb.db")
    return conn


def insert_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO t_book(title,publisher,page) VALUES(?,?,?)"
    cur.execute(sql, ('천개의 파랑', '천선란', 300))
    conn.commit()
    conn.close()

def delete_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "delete from t_book where book_no=?"
    cur.execute(sql, (1, ))
    conn.commit()
    conn.close()


def selcet_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM t_book"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)

    conn.close()


def selcet_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM t_book WHERE book_no=?"
    cur.execute(sql,(5, ))
    rs = cur.fetchone()
    print(rs)
    conn.close()


def update_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "update t_book SET book_no=? WHERE book_no=?"
    cur.execute(sql, (2, 4))
    conn.commit()
    conn.close()




if __name__=="__main__":
    #insert_book()
    #delete_book()
    #update_book()
    #selcet_book()
    selcet_one()

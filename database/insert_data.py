# 자료를 삽입하는 코드

from libs.db.dbconn import getconn

def insert_data():
    conn = getconn()      #db 연결
    cur = conn.cursor()

    # 자료 추가 - sql

    cur.execute("insert into member values ('철수', 20)")
    cur.execute("insert into member values ('짱구', 20)")


    conn.commit()
    conn.close()
if __name__ == "__main__":
    insert_data()
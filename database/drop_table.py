# Drop Table
from libs.db.dbconn import getconn

def drop_table():
    conn = getconn()
    cur = conn.cursor()

    # 테이블 삭제 - SQL DDL  > drop table 테이블이름
    sql = "drop table member"


    cur.execute(sql)

    conn.commit()
    conn.close()


if __name__ =="__main__":
    drop_table()
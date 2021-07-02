# 자료를 삽입하는 코드

from libs.db.dbconn import getconn

def insert_data():
    conn = getconn()      #db 연결
    cur = conn.cursor()

    # 자료 추가 - sql
    sql = "insert into member(mem_num,name,age) values(105,'유리',25)"
    # insert into 테이블이름(필드이름,필드이름,필드이름) values(데이터값,데이터값)
    cur.execute(sql)
    #cur.execute("insert into member values (103,'철수', 25)")
    #cur.execute("insert into member values (104,'짱구', 25)")


    conn.commit()
    conn.close()
if __name__ == "__main__":
    insert_data()
# member 테이블 전체 검색

from libs.db.dbconn import getconn

def select_data():
    conn = getconn()
    cur = conn.cursor()

    #자료 조회 spl DML (select)  select value,value( * = 전체) from 테이블이름
    sql ="select * from member"
    cur.execute(sql)

    print("데이터 전체 조회")

    rs = cur.fetchall() #저장된 자료를 꺼내옴
    for i in rs:
        print(i)

    conn.close()


if __name__ =="__main__":
    select_data()
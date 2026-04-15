import pymysql

def get_db():
    return pymysql.connect(host="192.168.100.20", user="Appsec", password="security", database="cju", cursorclass=pymysql.cursors.DictCursor)

def show_all():
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "SELECT m.name, g.subject, g.score, g.seq FROM member m JOIN grades g ON m.seq = g.member_seq"
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(f"번호:{row['seq']} | 학생:{row['name']} | 과목:{row['subject']} | 점수:{row['score']}")
    conn.close()

def add_score():
    m_seq = input("학생 번호(member_seq): ")
    sub = input("과목명: ")
    score = input("점수: ")
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "INSERT INTO grades (member_seq, subject, score) VALUES (%s, %s, %s)"
        cursor.execute(sql, (m_seq, sub, score))
    conn.commit()
    conn.close()
    print("추가 완료!")

def update_score():
    g_seq = input("수정할 성적 번호(seq): ")
    score = input("새 점수: ")
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "UPDATE grades SET score = %s WHERE seq = %s"
        cursor.execute(sql, (score, g_seq))
    conn.commit()
    conn.close()
    print("수정 완료!")

def delete_score():
    g_seq = input("삭제할 성적 번호(seq): ")
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "DELETE FROM grades WHERE seq = %s"
        cursor.execute(sql, (g_seq,))
    conn.commit()
    conn.close()
    print("삭제 완료!")

while True:
    print("\n1. 전체조회 2. 추가 3. 수정 4. 삭제 5. 종료")
    c = input("메뉴 선택: ")
    if c == '1': show_all()
    elif c == '2': add_score()
    elif c == '3': update_score()
    elif c == '4': delete_score()
    elif c == '5': break

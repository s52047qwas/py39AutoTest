import pymysql

class HandleDB:
    def __init__(self):
        self.conn =pymysql.connect(
            host='api.lemonban.com',
            port=3306,
            user='future',
            password='123456',
            db='futureloan'
        )
        self.cur = self.conn.cursor()

    def select_phone(self,phone):
        sql = 'select mobile_phone from member where mobile_phone={}'.format(phone)
        self.cur.execute(sql)
        result = self.cur.fetchall()

        self.cur.close()
        self.conn.close()

        return result

if __name__ == '__main__':
    a = HandleDB()
    name = a.select_phone(123456)
    print(type(name))
    if name:
        print('aa')
    else:
        print('a')
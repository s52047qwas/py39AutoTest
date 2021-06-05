import pymysql
from tools.handle_ini import conf

"""
单例模式：类似当时写日志时，
"""

class HandleDB:


    def __init__(self):
        mysql_info = dict(conf.items('mysql'))

        self.conn =pymysql.connect(
            host=mysql_info['host'],
            port=int(mysql_info['port']),
            user=mysql_info['user'],
            password=mysql_info['password'],
            db=mysql_info['db'],
            autocommit=True,##每次查询，拉取数据库最新信息
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()


    def get_one_data(self,sql,args=None):

        self.cur.execute(sql,args)
        return self.cur.fetchone()

    def get_all_data(self,sql,args=None):
        self.cur.execute(sql,args)
        return self.cur.fetchall()

    def get_many_data(self,sql):
        self.cur.fetchmany()


    def close(self):
        self.cur.close()
        self.conn.close()

    # def select_phone(self,phone):
    #     sql = 'select mobile_phone from member where mobile_phone={}'.format(phone)
    #     self.cur.execute(sql)
    #     result = self.cur.fetchall()
    #     return result,self.cur,self.conn

##单例模式
mysql = HandleDB()

if __name__ == '__main__':
    a = HandleDB()
    name = a.select_phone(123456)
    print(type(name))
    if name:
        print('aa')
    else:
        print('a')
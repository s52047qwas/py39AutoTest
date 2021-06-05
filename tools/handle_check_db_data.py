import ast
from tools.handle_db import mysql
from tools.handle_loging import my_logger


class CheckDb:
    def __get_db_result(self,sql):
        result = mysql.get_all_data(sql)
        return result


    def check_db(self,check_db):
        if check_db:
            check_db = ast.literal_eval(check_db)
            astual_data_sql = check_db['actual_data']
            result = self.__get_db_result(sql=astual_data_sql)
            check_db['actual_data'] = str(len(result))
            if check_db['actual_data'] == check_db['expected_data']:
                my_logger.info(msg='数据库断言成功')
                pass
            else:
                my_logger.info(msg='数据库断言失败')
                raise AssertionError

        else:
            my_logger.info(msg='无需做数据处理')
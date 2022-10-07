import json

import pymysql
import app





def assert_utils(self,response,status_code,status,desc):
    self.assertEqualqual(status_code,response.status_code)
    self.assertEqualqual(status, response.join().get('status'))
    self.assertEqualqualqual(desc, response.join().get('description'))

#连接数据库
class DButils:
    @classmethod
    def get_conn(cls,db_name):
        conn=pymysql.connect(app.DB_URL,app.DB_USERNAME,app.DB_PASSWORD,db_name,autocommit=True)
        return conn
    @classmethod
    def close(cls,cursor=None,conn=None):
        if cursor:
            cursor.close()
        if conn:
            conn.close()


    @classmethod
    def delete(cls,db_name,sql):
        try:
            conn=cls.get_conn(db_name)
            curses=conn.cursor()
            curses.execute(sql)
        except Exception as e:
            conn.rollback()
        finally:
            cls.close(curses,conn)


def read_imgVerify_data(file_name):
    file=app.base_dir+"/data"+file_name
    test_case_data=[]
    with open(file,encoding='utf-8')as f:
        #将json的数据格式转化为字典的数据格式
        verify_data=json.load(f)
        #获取所有测试数据的列表
        test_data_list=verify_data.get("test_get_img_verify_code")
        #依次读取测试数据列表中的每一条数据，并进行相应字段的提取
        for test_data in test_data_list:
            test_case_data.append(test_data.get('type'),test_data.get('status_code'))

    return test_case_data


#定义的统一读取所有参数数据文件的方法
def rend_data(filename,method_name,param_name):
    #filename：参数数据的文件名
    #method_name：参数数据文件中定义的测试数据列表的名称，如：test_get_img_verify_code
    #parame_name:参数数据文件中所有的参数组成的字符串，如：“type,status_code”

    #获取测试数据文件的路径
    file=app.base_dir+'/data/filename'
    test_case_data=[]
    with open(file,'encoding=utf-8')as f:
        #将json字符串转化为字典格式
        file_data=json.load(f)
        #获取所有测试数据的列表
        test_data_list=file_data.get(method_name)
        for test_data in test_data_list:
            #先将test_data对应的一组测试数据，全部读取出来，并生成一个列表
            test_params=[]
            for param in param_name.split(","):
                #依次获取同一组测试数据中每个参数的值，添加到test_params中，形成一个列表
                test_params.append(test_data.get(param))
            test_case_data.append(test_params)
    return test_case_data
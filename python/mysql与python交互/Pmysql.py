import  pymysql

class pMysql():
    def __init__(self,host,user,passwd,dbName):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.dbName=dbName

    def connet(self):
        self.db=pymysql.connect(self.host,self.user,self.passwd,self.dbName)
        self.cursor=self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self,sql):
        res=None
        try:
            self.connet()
            self.cursor.execute(sql)
            res=self.cursor.fetchone()
            self.close()
        except:
            print("查询失败")
        return res

    def get_all(self,sql):
        res=()
        try:
            self.connet()
            self.cursor.execute(sql)
            res=self.cursor.fetchall()
            self.close()
        except:
            print("查询失败")
        return res
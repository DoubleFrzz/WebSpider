import pymysql
from init_config import PraseConfig

CONF = PraseConfig()


class SqlHelper:
    def __init__(self):
        dictConfig = CONF.value_2_dict("db")
        self.conn = None
        self.cursor = None
        self.batch = int(dictConfig["write_batch"])
        try:
            self.conn = pymysql.connect(host=dictConfig["host"], port=int(dictConfig["prot"]),
                                        user=dictConfig["user"], passwd=dictConfig["passwd"], db=dictConfig["name"], charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception as e:
            self.db_error(e)
        else:
            print("Connect Database Is Success!")

    def create_table(self):
        pass

    def delete_table(self):
        pass

    def db_error(self, e, f):
        error = "%s : Error Code %d, %s" % (e.args[0], e.args[1])
        print(error)

    def _batch(self, datas):
        sql = "INSERT INTO `douban` (name,rank, moive_link, img_link, rate, judge_number, infomation, created_at) values "
        for data in datas[:-1]:
            sql += "(%s,now())," % ",".join(['"%s"' % i for i in data])
        sql += "(%s,now());" % ",".join(['"%s"' % i for i in datas[-1]])

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.db_error("_batch", e)
            self.conn.rollback()

    def insert(self, datas):
        length = len(datas)
        loop = length // self.batch
        end = 0
        for i in range(loop):
            start = i * self.batch
            end = (i+1) * self.batch
            self._batch(datas=datas[start:end])
        self._batch(datas=datas[end:])
        print("Write To Database Is Success!")

    def select_all(self):
        sql = "SELECT * FROM `douban`;"
        data = ()
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        except Exception as e:
            self.db_error("select_all", e)
        else:
            print("Select Is Success!")
        return data

    def __del__(self):
        if self.conn:
            self.conn.close()
        print("SqlHelper Destory")


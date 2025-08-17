import psycopg2


class PostGreSqlUtils:
    def __init__(self):
        # 连接到 PostgreSQL 数据库
        self.conn = psycopg2.connect(
            dbname="xykywdb",
            user="batchuser",
            password="Hrbb_1234",
            host="130.1.11.183",
            port="51000"
        )

    def query_sql(self, sql, *args):
        # 创建一个游标对象
        cur = self.conn.cursor()

        # 执行 SQL 查询
        cur.execute(sql, *args)

        # 获取查询结果
        postgresql_results = []
        rows = cur.fetchall()
        for row in rows:
            postgresql_results.append(row)

        # 关闭游标和连接
        cur.close()
        self.conn.close()
        return postgresql_results

    def execute_sql(self, sql, *args):
        cursor = self.conn.cursor()
        cursor.execute(sql, (*args,))
        self.conn.commit()
        cursor.close()

# if __name__ == '__main__':
#     sql = "SELECT * FROM t_dc_mobile_info WHERE id_no ='622123198212012753'"
#     PostGreSqlUtils = PostGreSqlUtils()
#     postgresql_results =PostGreSqlUtils.query_sql(sql)
#     print(postgresql_results)

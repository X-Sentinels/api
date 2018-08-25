import pymysql
from config import db_config,args_curl,args_ping,user


def data_query(tables):
    con = pymysql.connect(**db_config)
    cursor = con.cursor()
    if tables == "users":
        try:
            sql = """select * from users"""
            cursor.execute(sql)
        except:
            print("There is no table named users")
            con.rollback()
        row_users = cursor.fetchall()
        # con.close()
        user_list=list()
        for i in range(len(row_users)):
            user_dict = dict()
            for j in range(len(user)):
                user_dict[user[j]]=row_users[i][j]
            user_list.append(user_dict)
        return user_list
    elif tables == "args_ping":
        try:
           sql = """select * from args_ping"""
           cursor.execute(sql)
        except:
            print("There is no table named args_ping")
            con.rollback()
        row_ping = cursor.fetchall()
        # con.close()
        ping_list = list()
        for i in range(len(row_ping)):
            ping_dict = dict()
            for j in range(len(args_ping)):
                if j==0:
                    continue
                ping_dict[args_ping[j]] = row_ping[i][j]
            ping_list.append(ping_dict)
        return ping_list

    elif tables == "args_curl":
        try:
             sql = """select * from args_curl """
             cursor.execute(sql)
        except:
            print("There is no table named args_curl")
            con.rollback()
        row_curl = cursor.fetchall()
        # con.close()
        curl_list = []
        for i in range(len(row_curl)):
            curl_dict = {}
            for j in range(len(args_curl)):
                curl_dict[args_curl[j]] = row_curl[i][j]
            curl_list.append(curl_dict)
        return curl_list



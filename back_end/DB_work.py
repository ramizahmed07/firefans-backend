from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

dbconfig = read_db_config()
conn = MySQLConnection(**dbconfig)
cursor = conn.cursor()
def insert_values():
    for i in range(54,105):

        cursor.execute("UPDATE `verification` SET `verified` = '" + str(1) + "' WHERE user_id=" + str(i) + ";")
        conn.commit()
        print("done updating verified for user "+str(i))
        cursor.execute("INSERT INTO `user_data` (`user_id`, `website`, `bio`, `tag_1`, `tag_2`, `tag_3`, `tag_4`, `tag_5`, `facebook`, `twitter`, `instagram`, `youtube`) VALUES ('"+str(i)+"', '', '', '', '', '', '', '', '', '', '', '')")
        conn.commit()
        print("\n \n"+"done updating verified for user " + str(i))

        #cursor.execute("INSERT INTO `profile_photo` (`pic_id`, `user_id`, `profile_pic`) VALUES  (NULL, '" + str(i) + "', 'null');")
        #conn.commit()
        #cursor.execute("INSERT INTO `cover_photo` (`pic_id`, `user_id`, `cover_pic`) VALUES  (NULL, '" + str(i) + "', 'null');")
        #conn.commit()


insert_values()
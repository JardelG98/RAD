import sqlite3 #importar biblioteca sqlite
banco = sqlite3.connect('database.db')
cursor = banco.cursor()
#cursor.execute("CREATE TABLE cliente ( nome text, idade integer, sex text)")
#cursor.execute("INSERT INTO cliente VALUES ('Jardel',25,'m'),('Antonio',26,'m')")
cursor.execute("SELECT * from cliente")
print(cursor.fetchall())
banco.commit()
cursor.close() #fecha o cursor
banco.close()  #fecha conexão
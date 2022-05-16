
import psycopg2



while True:
    conn = psycopg2.connect(
        host="host",
        database="dbname",
        user="username",
        password="*",
        port="8080")
    cur = conn.cursor()
    x = int(input("Action\n1. Initialize data\n2. getRoomById\n3. getAllRoom\n4. getChatById\n5. getAllChatInRomm\n0. Exit\nSelect the action: "))

    if(x == 1):
        cur.execute("SELECT * FROM public.chatevent;")
        print(conn)
        cur.close()
    elif(x == 2):
        y = int(input("getroomId: "))
        cur.execute("SELECT * FROM public.room WHERE id = %s",(y,))
        if(cur.rowcount > 0 ):
            print(cur.fetchall())
        else:
            print("No Room with id: ",y)
    elif(x == 3):
        cur.execute("SELECT * FROM public.room ")
        print(cur.fetchall())
    elif(x == 4):
        y = int(input("getchatId: "))
        cur.execute("SELECT * FROM chatevent WHERE id = %s",(y,))
        if(cur.rowcount > 0 ):
            print(cur.fetchall())
        else:
            print("No Chat with id: ",y)
    elif(x == 5):
        y = int(input("getRoomId: "))
        cur.execute("SELECT sender, message FROM chatevent cv left join room rm on cv.roomid = rm.id where rm.id = %s ",(y,))
        print(cur.fetchall())
    elif(x == 0):
        break
    else:
        print("No Choice with Number")


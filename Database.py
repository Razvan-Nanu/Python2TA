import sqlite3

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS file_name(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        text_name TEXT)")
    conn.commit()
    conn = sqlite3.connect('test.db')
    #tuple Name
    fileList = ('info.docx', 'Hello.txt', 'myImage.png', \
                'Movie.mpg', 'world.txt', 'data.pdf','photo.jpg')
    #loop through each extension to find .txt
    for x in fileList:
        if x.endswith('.txt'):
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO file_name (text_name) VALUES(?)", (x,))
                print(x)

conn.close()





import sqlite3

con = sqlite3.connect('youtube_videos.db')

cursor = con.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_videos():
    cursor.execute('''
    SELECT * FROM videos
''')
    for row in cursor.fetchall():
        print(row)

def add_videos(name, time):
    cursor.execute(f'''
    INSERT INTO videos (name,time) VALUES(
                   ?,?)
''',(name,time))
    con.commit()

def update_videos(index,name,time):
    cursor.execute('''
    UPDATE videos SET name = ?, time = ? WHERE id = ?
''',(name,time,index))
    con.commit()

def delete_videos(index):
    cursor.execute('''
    DELETE FROM videos WHERE id = ?
''',(index,))
    con.commit()

def main():
    while True:
        print("\nYoutube Manager app with db")
        print("1. List videos")
        print("2. Add vidoes")
        print("3. Update vidoes")
        print("4. Delete videos")
        print("5. Exit app")

        choice = input("Enter your choice -> ")

        match(choice):
            case "1":
                list_videos()
            case "2":
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_videos(name, time)
            case "3":
                list_videos()
                index = input("Enter video id. to be updated: ")
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                update_videos(index,name,time)
            case "4":
                list_videos()
                index = input("Enter video id to be deleted: ")
                delete_videos(index)
            case "5":
                break
            case _:
                print("Invalid choice!")
    con.close()

if __name__ == "__main__":
    main()
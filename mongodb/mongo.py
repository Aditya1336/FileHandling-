from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.3clparr.mongodb.net/",tlsAllowInvalidCertificates=True)

db = client['ytmanager']

video_collection = db['videos']

def list_all_videos():
    for video in video_collection.find():
        print(f"Id:{video['_id']}, Name:{video['name']}, time:{video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name":name,"time":time})

def update_video(index,name,time):
    video_collection.update_one(
        {'_id':ObjectId(index)},
        {"$set":{"name":name, "time":time}})

def delete_video(index):
    video_collection.delete_one({'_id':ObjectId(index)})


def main():
    while(True):
        print("\nYoutube manager app")
        print("1. List all videos")
        print("2. Add new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

        choice = input("Enter a choice : ")

        match(choice):
            case "1":
                list_all_videos()
            case "2":
                name = input("Enter video name : ")
                time = input("Enter video time : ")
                add_video(name, time)
            case "3":
                index = input("Enter the video id. : ")
                name = input("Enter updated video name : ")
                time = input("Enter updated video time : ")
                update_video(index,name,time)
            case "4":
                index = input("Enter the video id. : ")
                delete_video(index)
            case "5":
                break
            case _:
                print("Invalid Choice")



if __name__ == "__main__":
    main()
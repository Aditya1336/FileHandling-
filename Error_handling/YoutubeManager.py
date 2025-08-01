import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    for index, video in enumerate(videos,start=1):
        print(f"{index}. {video.get('name')}")

def add_videos(videos):
    name = input("Enter video name : ")
    time = input("Enter video time : ")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input('Enter the video no. you want to update : '))
    if 1<= index <=len(videos):
        name = input("Enter the new video name : ")
        time = input("Enter the new video time : ")
        videos[index-1] = {'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected.")

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video no> to be deleted : "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected.")

def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager ")
        print("1. List of favourite videos.")
        print("2. Add a youtube video.")
        print("3. Update a youtube video.")
        print("4. Delete a youtube video.")
        print("5. Exit the app.")
        choice = input("Enter a choice : ")

        match(choice):
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Enter a valid choice")

if __name__ == '__main__':
    main()

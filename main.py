def all_videos(videos):
    pass


def add_video(videos):
    pass


def update_video(videos):
    pass


def delete_video(videos):
    pass


videos = []
while True:
    print("\nWelcome to Youtube Manager")
    print("1. List All Youtube Videos")
    print("2. Add a Youtube Video")
    print("3. Update Youtube Video Details")
    print("4. Delete a Youtube Video")
    print("5. Exit From App")
    choice = input("Enter Your Choice: ")

    match choice:
        case "1":
            all_videos(videos)
        case "2":
            add_video(videos)
        case "3":
            update_video(videos)
        case "4":
            delete_video(videos)
        case "5":
            break
        case _:
            print("Invalid Choice")

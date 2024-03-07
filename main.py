import json

yt = "youtube.txt"


def load_data():
    try:
        with open(yt, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# helper
def save_data_helper(videos):
    with open(yt, "w") as file:
        json.dump(videos, file)


def all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Time: {video['time']}")


def add_video(videos):
    name = input("enter video name")
    time = input("enter video time")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    pass


def delete_video(videos):
    pass


def main():
    videos = load_data()
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


if __name__ == "__main__":
    main()

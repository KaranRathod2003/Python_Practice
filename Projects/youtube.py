def load_video_data():
    pass

def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass


def main():
    videos = load_video_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        # print(videos)

        match (choice):
            case ('1'):
               list_all_videos() 
            case ('2'):
               add_video() 
            case ('3'):
                update_video()
            case ('4'):
                delete_video() 
            case ('5'):
                break
            case (_):
                print("Invalid Point !!!")
        # end match

if __name__ == "__main__":
    main()

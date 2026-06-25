import os

folder=input("Enter folder path:")
if os.path.exists(folder):
        files = os.listdir(folder)

        if len(files) == 0:
            print("Folder is empty.")
        else:
            print("\nFILES IN THE DIRECTORY:\n")
            for index, file in enumerate(files, start=1):
                print(f"{index}. {file}")
else:
    print("Folder does not exist.")
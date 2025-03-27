import os

file_types = {
    "audio": [".mp3", ".wav", ".flac"],
    "video": [".mp4", ".mkv", ".avi"],
    "document": [".doc", ".pdf", ".txt"],
    "image": [".jpg", ".jpeg", ".png"],
    "compressed": [".zip", ".rar", ".7z"],
    "executable": [".exe", ".msi"],
    "spreadsheet": [".xls", ".xlsx", ".csv"],
    "presentation": [".ppt", ".pptx"],
    "code": [".py", ".java", ".c", ".cpp", ".html", ".css", ".js", ".ts"],
}

def create_folder(folder_name) -> None:
    try:
        os.mkdir(folder_name)
        print(f"Folder {folder_name} created.")
    except FileExistsError:
        print(f"Folder {folder_name} already exists.")

def delete_folder(folder_name) -> None:
    basename = os.path.basename(folder_name)
    try:
        os.rmdir(folder_name)
        print(f"Folder {basename} removed.")
    except FileNotFoundError:
        print(f"Folder {basename} does not exist.")
    except OSError:
        print(f"Folder {basename} can not be removed.")

def move_file(file_path, destination_path, file_name) -> None:
    try:
        os.rename(file_path, os.path.join(destination_path, file_name))
        print(f"File {file_name} moved to {destination_path}")
    except FileExistsError:
        print(f"File {file_name} already exists in {destination_path}")
    except FileNotFoundError:
        print(f"File {file_name} not found in {file_path}")
    except PermissionError:
        print(f"Permission denied for {file_name}")


def flatten(origin_path, current_path) -> None:
    #print("origin:", origin_path, "current:", current_path)
    for entry in os.scandir(current_path):
        #print(f"Processing file: {entry.name}")
        if entry.is_dir():
            flatten(origin_path, entry.path)
            delete_folder(entry.path)
        else:
            # Skip if the file is already in the top directory
            if entry.path == os.path.join(origin_path, entry.name):
                continue
            print(f"Moving file: {entry.name} to {os.path.join(origin_path, entry.name)}")
            move_file(entry.path, origin_path, entry.name)

def orderByType(path) -> None:
    for entry in os.scandir(path):
        if entry.is_file():
            extension = os.path.splitext(entry.name)[1]
            print(f"Processing file: {entry.name} - Type: {extension}")
            
            # Determine the destination folder based on the file's extension
            destination_folder = None
            for key, values in file_types.items():
                if extension in values:
                    destination_folder = os.path.join(path, key)
                    break

            if destination_folder is None:
                destination_folder = os.path.join(path, "others")
            
            if not os.path.exists(destination_folder):
                print(f"Creating folder: {destination_folder}")
                create_folder(destination_folder)
            
            move_file(entry.path, destination_folder, entry.name)

def main():
    path = os.path.join(os.getcwd(), 'test')

    while True:
        option = input("1.- Flatten\n2.- Order by type\n: ")
        if option not in ["1", "2"]:
            break
        if option == "1":
            flatten(path, path)
        elif option == "2":
            orderByType(path)
        else:
            print("Invalid option.") 

if __name__ == "__main__":
    main()
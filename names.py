import os


def getNameAndStore():
    # Get the person's name from the user
    person_name = input("Enter the person's name: ")

    # Write the person's name to a file
    with open("names.txt", "a") as file:
        file.write(person_name+'\n')

    # print("Person's name has been stored in temp.txt.")

# if __name__ == "__main__":
#     main()



def fetch_names_from_file(filename):
    try:
        # Open the file for reading
        with open(filename, "r") as file:
            # Read all lines from the file
            names = file.readlines()
            # Strip newline characters and any leading/trailing whitespace from each name
            names = [name.strip() for name in names]
            return names
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

# def main():
#     # Specify the filename
#     filename = "names.txt"

#     # Fetch names from the file
#     names = fetch_names_from_file(filename)

#     # Print the fetched names
#     if names:
#         print("Names stored in temp.txt:")
#         # for name in names:
#         print(names)
#     else:
#         print("No names found in temp.txt.")

# if __name__ == "__main__":
#     main()


def delete_files_in_directory(directory):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        # Check if the file path is a regular file (not a directory)
        if os.path.isfile(file_path):
            # Delete the file
            os.remove(file_path)

    

def deleteNames(file):
    with open(file, 'w') as f:
        f.write("\n")
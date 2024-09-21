# file_handling_assignment.py

def create_file():
    try:
        # Create a new text file in write mode
        with open('my_file.txt', 'w') as file:
            file.write("Hello, this is my first line.\n")
            file.write("Here is a number: 42.\n")
            file.write("And another line with text.\n")
        print("File created and written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred while creating the file: {e}")
    finally:
        print("Finished attempting to create the file.")

def read_file():
    try:
        # Read the contents of the file and display them
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File Contents:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        print("Finished attempting to read the file.")

def append_to_file():
    try:
        # Open the file in append mode and add new lines
        with open('my_file.txt', 'a') as file:
            file.write("Appending a new line of text.\n")
            file.write("Here's another line with the number: 100.\n")
            file.write("Final line added to the file.\n")
        print("File updated successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("Finished attempting to append to the file.")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read again to display updated contents

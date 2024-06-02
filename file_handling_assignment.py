"""
    File Handling Assignment
"""

def create_file():
    try:
        # Create a new file in write mode ('w')
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is line 1.\n")
            file.write("12345\n")
            file.write("Python is awesome!\n")
        print("File created successfully.")
    except Exception as e:
        print(f"Error creating the file: {e}")
    finally:
        print("File creation process completed.")

def read_and_display():
    try:
        # Read the contents of the file
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\nContents of my_file.txt:")
            print(content)
    except FileNotFoundError:
        print("File not found. Please create it first.")
    except Exception as e:
        print(f"Error reading the file: {e}")
    finally:
        print("File reading process completed.")

def append_to_file():
    try:
        # Append additional lines to the file
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1.\n")
            file.write("98765\n")
            file.write("Python is versatile!\n")
        print("\nFile updated successfully.")
    except Exception as e:
        print(f"Error appending to the file: {e}")
    finally:
        print("File appending process completed.")

if __name__ == "__main__":
    create_file()
    read_and_display()
    append_to_file()

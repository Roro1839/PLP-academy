# File Handling Assignment Script

try:
    # Step 1: File Creation
    with open("my_file.txt", "w") as file:
        file.write("Line 1: This is a test.\n")
        file.write("Line 2: Including a mix of strings and numbers: 42\n")
        file.write("Line 3: Another line of text.\n")

    # Step 2: File Reading and Display
    print("\nReading and displaying the contents:")
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)

    # Step 3: File Appending
    print("\nAppending additional lines to the file:")
    with open("my_file.txt", "a") as file:
        file.write("Line 4: Appended line 1.\n")
        file.write("Line 5: Appended line 2.\n")
        file.write("Line 6: Final appended line.\n")

    # Re-read and display the updated content
    print("\nUpdated content after appending:")
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("Permission denied to access the file.")
finally:
    print("Script execution completed.")



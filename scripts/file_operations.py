import os
import os.path


def read_file(filename):
    """Read a file and return the contents"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        return "Error: " + str(e)


def write_to_file(filename, text):
    """Write text to a file"""
    try:
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(filename, "w") as f:
            f.write(text)
        return "File written successfully."
    except Exception as e:
        return "Error: " + str(e)


def append_to_file(filename, text):
    """Append text to a file"""
    try:
        with open(filename, "a") as f:
            f.write(text)
        return "Text appended successfully."
    except Exception as e:
        return "Error: " + str(e)


def delete_file(filename):
    """Delete a file"""
    try:
        os.remove(filename)
        return "File deleted successfully."
    except Exception as e:
        return "Error: " + str(e)


def search_files(directory=""):
    """Search for files in a directory"""
    found_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.startswith("."):
                continue
            relative_path = os.path.relpath(os.path.join(root, file), directory)
            found_files.append(relative_path)

    return found_files

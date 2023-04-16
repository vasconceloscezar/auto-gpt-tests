import os
import os.path


def read_file(filename):
    """Read a file and return the contents"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        print(content)
    except Exception as e:
        print("Error: " + str(e))


if __name__ == "__main__":
    testFile = "./auto_gpt_workspace/design.txt"
    read_file(testFile)

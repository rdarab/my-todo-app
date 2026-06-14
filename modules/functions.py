FILEPATH = "todos.txt"
def read_file(filepath=FILEPATH):
    """
    Read a text in a file and return it as a list of to-do items.
    """
    try:
        with open(filepath, 'r') as f:  # creating the file object in read mode
            todos_list = f.readlines()
            return todos_list
    except FileNotFoundError:
        exit("File not found.")

def write_to_file(re_todos, filepath=FILEPATH):
    """
    Write a text in a file and return it as a list of to-do items.
    """
    with open(filepath, 'w') as f:
        f.writelines(re_todos)

# these two lines now are only executed when functions.py file is executed directly
# and these lines are not executed when you execute the other script
# which imports the functions.py file.
if __name__ == "__main__":
    print("Hello")
    print(read_file())
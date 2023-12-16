# Reading prompts from files
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"The file at path '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
file1_path = "./../prompts/input.txt"
file2_path = "./../prompts/output.txt"
file3_path = "./../prompts/system.txt"

input_prompt = read_file(file1_path)
ouput_prompt = read_file(file2_path)
system_prompt = read_file(file3_path)

# Now, content1, content2, and content3 contain the content of the respective files
if input_prompt is not None:
    print(f"Content of file 1:\n{input_prompt}")

if ouput_prompt is not None:
    print(f"Content of file 2:\n{ouput_prompt}")

if system_prompt is not None:
    print(f"Content of file 3:\n{system_prompt}")

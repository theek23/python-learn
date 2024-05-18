import subprocess
import random
import string


def generate_random_message(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def create_and_edit_file(filename):
    with open(filename, 'w') as file:
        file.write("This is a sample text file.\n")

def run_git_commands(message):
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])

def main():
    num_commits = int(input("How many commits do you need? "))
    filename = "sample.txt"

    for _ in range(num_commits):
        create_and_edit_file(filename)
        commit_message = generate_random_message()
        run_git_commands(commit_message)
        print(f"Commit with message '{commit_message}' has been created.")

if __name__ == "__main__":
    main()

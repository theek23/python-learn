import subprocess
import random
import string
import time

def generate_random_message(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def create_and_edit_file(filename):
    with open(filename, 'a') as file:  # Change mode to 'a' to append to the file
        timestamp = time.time()  # Get the current time as a unique identifier
        file.write(f"Modification at {timestamp}\n")  # Append a unique line

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

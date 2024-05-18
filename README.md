
# Git Commit Bot 🚀

Welcome to the Git Commit Bot! This Python script automates the creation of multiple git commits with ease. Follow the steps below to get started and supercharge your commit workflow.

## Getting Started
### Prerequisites

Make sure you have the following installed on your machine:

- Python 🐍
- Git 🔧

### Step 1: Initialize Your Repository
First, navigate to your project directory and initialize a new Git repository:

git init

```bash
    git init
```

    
### Step 2: Clone This Repository
If you haven't already, clone this repository to your local machine:

```bash
    git clone https://github.com/yourusername/git-commit-bot.git
    cd git-commit-bot
```

### Step 3: Run the Python Script
Run the run.py script to start the bot:

```bash
    python run.py
```

### Step 4: Enter the Number of Commits
When prompted, enter the number of commits you need:

```bash
    How many commits do you need? 5
```

### Step 5: Watch the Magic Happen ✨
The bot will create and commit the specified number of changes to your repository. Each commit will have a unique, randomly generated message.

### Step 5: Step 6: Push to GitHub 🚀
Once the commits are created, push them to your GitHub repository:

```bash
    git remote add origin https://github.com/yourusername/your-repo.git
    git push -u origin main
```
## How It Works
- Random Commit Messages: Each commit message is a random string of 10 lowercase letters.
- File Modifications: The bot appends a unique timestamp to sample.txt with each commit, ensuring a different change every time.
- Automated Git Commands: The script handles git add and git commit for you.

## Example Output

```bash
    Commit with message 'abcxyzdefg' has been created.
    Commit with message 'hijklmnopq' has been created.
    Commit with message 'rstuvwxyza' has been created.
    Commit with message 'bcdefghijk' has been created.
    Commit with message 'lmnopqrst' has been created.
```

## Customization

Feel free to modify the script to suit your needs. Whether it’s changing the commit message format or the file being edited, this bot is flexible and easy to adapt.

## Contribution

Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.

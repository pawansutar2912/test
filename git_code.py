# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:39:02 2024

@author: sutar1
"""
import os
import shutil
import subprocess

# GitHub repository URL
repo_url = "https://github.com/pawansutar2912/test.git"

# Path to the file you want to add
file_to_add = "C:/pawan/GAB/git_code.py"  # Change this to the actual path of your file

# Check if the file exists
if not os.path.exists(file_to_add):
    print("File does not exist:", file_to_add)
    exit(1)

# Clone the repository to a temporary directory
temp_dir = "temp_repo"
subprocess.run(["git", "clone", repo_url, temp_dir])

# Change working directory to the cloned repository directory
os.chdir(temp_dir)

# Initialize the repository if it's empty
if not os.listdir("."):
    subprocess.run(["git", "init"])
    subprocess.run(["git", "remote", "add", "origin", repo_url])

# Add the file to the repository directory
shutil.copy(file_to_add, ".")

# Add the file to git staging area
subprocess.run(["git", "add", "."])

# Commit the changes
commit_msg = "python code added"
subprocess.run(["git", "commit", "-m", commit_msg])

# Push to GitHub
push_result = subprocess.run(["git", "push", "-u", "origin", "HEAD:master"], capture_output=True)

# Check if the push was successful
if push_result.returncode == 0:
    print("File added successfully and pushed to GitHub.")
else:
    print("Failed to push changes to GitHub:")
    print(push_result.stderr.decode())

# C:/pawan/GAB/sample.txt
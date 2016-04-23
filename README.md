# Synopsis
LazyGit is to be used to automate the process of pushing code from local repository to remote repository.
Very useful for personal projects.
To skip password authentication while pushing code you need to have an SSH key linked to your GitHub account. 
For generating your own SSH key check out [Generating an SSH key](https://help.github.com/articles/generating-an-ssh-key/).

# How to Use
1. Clone <code>LazyGit</code>
2. Navigate to the directory where <code>lazy_git</code> is cloned. <code>cd LazyGit </code>
3. Run <code>python lazy_git new</code> to setup your git_username and git_reponame.
4. Run <code>python lazy_git.py \<checkout_directory\> </code>

# Code Example
2 system arguments are required for running LazyGit :

- file name (always lazy_git.py)
- checkout_directory 

> python lazy_git.py \<checkout_directory\> 

Eg : <code> python lazy_git.py /home/mayank/Desktop/LazyGit </code>

# Motivation
Pushing code from a local repository to an upstream was a tedious task. 
I've developed this script to make the whole process easier and less time consuming.

# Screenshots
![alt tag](https://github.com/mayank26saxena/LazyGit/blob/master/screenshots/screenshot1.png)
![alt tag](https://github.com/mayank26saxena/LazyGit/blob/master/screenshots/screenshot4.png)

That awesome moment when I used lazy\_git.py to push lazy_git.py :laughing:

# Task Lists
- [ ] Submit package to PyPi.
 

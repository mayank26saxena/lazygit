# Synopsis
LazyGit is to be used to automate the process of pushing code from local repository to remote repository. 
To skip password authentication while pushing code you need to have an SSH key linked to your GitHub account. 
For generating your own SSH key check out [Generating an SSH key](https://help.github.com/articles/generating-an-ssh-key/).

# How to Use
1. Clone <code>LazyGit</code>
2. Replace your <code>git_username</code> && <code>git_reponame</code> in the file and save.
3. Navigate to directory where <code>lazy_git</code> is cloned.
4. Run <code>python lazy_git.py \<checkout_directory\> \<local_repo_name\></code>

# Code Example
3 system arguements are required for running LazyGit :

- file name (always lazy_git.py)
- checkout_directory 
- local repo_name

> python lazy_git.py \<checkout_directory\> \<local_repo_name\>

Eg : <code> python lazy_git.py /home/mayank/Desktop/LazyGit LazyGit </code>

# Motivation
Pushing code from local repository to upstream was a tedious task. 
I've developed this script to make the whole process easier and less time consuming.

# Screenshot
![alt tag](https://github.com/mayank26saxena/LazyGit/blob/master/screenshots/screenshot2.png)
![alt tag](https://github.com/mayank26saxena/LazyGit/blob/master/screenshots/screenshot1.png)

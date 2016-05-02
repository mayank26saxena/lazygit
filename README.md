# LazyGit
LazyGit is to be used to automate the process of pushing code from local repository to remote repository.
Very useful for personal projects.
To skip password authentication while pushing code you need to have an SSH key linked to your GitHub account. 
For generating your own SSH key check out [Generating an SSH key](https://help.github.com/articles/generating-an-ssh-key/).

[![PyPI](https://img.shields.io/badge/PyPi-v1.1-f39f37.svg)](https://pypi.python.org/pypi/lazygit)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://doge.mit-license.org/)


# Install

### Using pip
<code> pip install lazygit </code>

### Using Git
<code>git clone https://github.com/mayank26saxena/LazyGit.git</code>

<code>cd lazygit</code>

<code>python setup.py install</code>

# How to Use
1. Run <code>pip install lazygit</code> to install.
2. Run <code>lazygit new</code> to setup username and reponame. 
3. Run <code>python lazygit \<checkout_directory\> </code>
4. Write commit message.
5. Voila! Your commit has been pushed.

# Motivation
Pushing code from a local repository to an upstream was a tedious task. 
I've developed this script to make the whole process easier, user friendly and less time consuming.

# Code Example
<code>lazygit new</code>
> Enter your GitHub username : mayank26saxena

> Enter Github remote repository name : LazyGit

<code>lazygit /home/mayank/Desktop/LazyGit</code>
> Write your commit message : Removed backup files.

![alt tag](https://github.com/mayank26saxena/LazyGit/blob/master/screenshots/screenshot3.png)

# Screenshots
![alt tag](https://github.com/mayank26saxena/LazyGit/blob/master/screenshots/screenshot2.png)

That awesome moment when I used lazy\_git.py to push lazy_git.py :sunglasses:

# Task Lists
- [X] Submit package to PyPi.
- [X] Add support for Python 3+.
- [X] Option to make commit on a branch. Default branch is master.  
- [ ] Add git pull operation before push.
 
# Contributing
Use github's Pull request/issues feature for all contributions.

import os
import sys
from git import Repo

"""
You need to have a valid SSH key added to your GitHub account
This key serves as a fingerprint and password authentication is skipped while pushing code
If SSH key has not been added then you will be prompted for password while pushing

To set up git_username and git_reponame run python lazy_git.py new

For running LazyGit -
3 system arguements are required
Argument[0] - file name ie lazy_git.py
Argument[1] - checkout_directory 

To run locally, execute the following command:
python lazy_git.py <checkout_directory> <local_repo_name>

"""

#Keywords
git_remote_command = 'git remote set-url origin git@github.com:'
slash = "/"
git = ".git"

def main():
    if len(sys.argv) == 2 :
        text = sys.argv[1]
        text = text.lower()
        if text == 'new' :
            #Write git_username and git_reponame to info.txt file
            f = open('info.txt' , 'w')
            git_username = input('Enter your GitHub username : ')
            f.write(git_username)
            f.write(os.linesep)
            git_reponame = input('Enter GitHub remote repository name : ')
            f.write(git_reponame)
            f.close()

        else :
    
            checkout_dir = sys.argv[1]
            commit_msg = input('Write your commit message: ')


            repo = Repo(checkout_dir)
            branch = repo.active_branch
            print (branch.name)

            #Retrieve git_username and git_reponame from info.txt file
            
            file_name = 'info.txt'
            with open(file_name) as f:
                content = f.readlines()

            content = [x.strip('\n') for x in content]

            git_username = content[0]
            git_reponame = content[1]

            url = git_remote_command + git_username + slash + git_reponame + git
        
            #Path to local repository
            #path =  checkout_dir + '/' + repo_name + '/'
        
            os.chdir('%s' %checkout_dir)
	
            #Printing current wokring directory
            print ('Current working directory is : ')
            os.system('pwd')        
        
            #Check whether git has been initialised in directory
            n = os.system('git rev-parse')
            #print n 
        
            #If n == 0 git has been initialised already	
            #If n != 0 initialise git and add set remote repo URL
            if n != 0 :
                print 'Current working directory is - '
                os.system('pwd')
                os.system('git init')
                os.system('git remote add origin https://github.com/' + git_username + slash + git_reponame + git)
                os.system('git remote add origin git@github.com:' + git_username + slash + git_reponame + git)
                os.system(url)
            
            txt = """#!/bin/sh

GIT_WORK_TREE = %s git checkout -f""" %checkout_dir

            #Run git add, commit, push
            os.system('git add .')
            os.system('git commit -m \'' + commit_msg + '\'')
            os.system('git push origin '+ branch.name)

if __name__ == "__main__" :
    main()


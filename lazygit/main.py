import os
import sys
from git import Repo
from builtins import input
from appdirs import *

"""
You need to have a valid SSH key added to your GitHub account
This key serves as a fingerprint and password authentication is skipped while pushing code
If SSH key has not been added then you will be prompted for password while pushing

To set up git_username and git_reponame run -
python lazygit new

To push code to remote repository run - 
lazygit <checkout_dir>
"""

#Keywords
usage_message = 'usage: lazygit [new|check-out-directory]'
checkout_dir_error = 'checkout_dir does not exist'
git_remote_command = 'git remote set-url origin git@github.com:'
slash = "/"
git = ".git"


appname = "lazygit"
appauthor = "MayankSaxena"

info_dirname = user_data_dir(appname, appauthor)
info_filename = info_dirname + '/info.txt' 

def main():
    if not os.path.exists(info_dirname) :
       os.makedirs(info_dirname)

    try :
      assert len(sys.argv) == 2 
    except AssertionError as e:
        print(usage_message)
        return
    commandname =  sys.argv[1]
    commandname = commandname.lower()
    if commandname == 'new' :
            #Write git_username and git_reponame to info.txt file
            f = open(info_filename , 'w')
            git_username = input('Enter your GitHub username : ')
            f.write(git_username)
            f.write(os.linesep)
            git_reponame = input('Enter GitHub remote repository name : ')
            f.write(git_reponame)
            f.close()

    else :
            checkout_dir = sys.argv[1]
            if not os.path.exists(checkout_dir) :
               print(checkout_dir_error)
               return

            commit_msg = input('Write your commit message: ')
            repo = Repo(checkout_dir)
            branch = repo.active_branch
            print ('Active branch name is: ',branch.name)

            #Retrieve git_username and git_reponame from info.txt file

            with open(info_filename) as f:
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

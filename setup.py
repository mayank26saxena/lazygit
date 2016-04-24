from distutils.core import setup
setup(
  name = 'lazygit',
  packages = ['lazygit'], # this must be the same as the name above
  version = '0.2',
  description = 'Automating the daily git push operations',
  author = 'Mayank Saxena',
  author_email = 'mayank26saxena@gmail.com',
  url = 'https://github.com/mayank26saxena/LazyGit', # use the URL to the github repo
  download_url = 'https://github.com/mayank26saxena/LazyGit/tarball/0.1', # I'll explain this in a second
  keywords = ['github', 'push', 'commit', 'lazygit'], # arbitrary keywords
  classifiers = [],
  install_requires=[
        "os",
        "system"
  ],  
  entry_points={
        'console_scripts': [
            'lazygit = lazygit.lazy_git:main'
        ],
  }
)

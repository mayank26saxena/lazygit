from setuptools import setup
setup(
  name = 'lazygit',
  packages = ['lazygit'], # this must be the same as the name above
  version = '0.6',
  description = 'Automating the daily git push operations',
  author = 'Mayank Saxena',
  author_email = 'mayank26saxena@gmail.com',
  url = 'https://github.com/mayank26saxena/LazyGit', # use the URL to the github repo
  download_url = 'https://github.com/mayank26saxena/LazyGit/tarball/0.6', # I'll explain this in a second
  keywords = ['github', 'push', 'commit', 'lazygit'], # arbitrary keywords
  classifiers = [],
  entry_points={
        'console_scripts': [
            'lazygit = lazygit.main:main'
        ],
  },
  install_requires=[
      'gitpython',
  ]
)

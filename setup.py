try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = [
    'description': 'A simple python text-based adventure game.',  
    'author': 'Marc-Andre Charland',
    'nick_name': 'Macpoule'
    'url': 'URL to get it at.',  # add
    'download_url': 'Where to download it.', # add
    'author_email': 'macpoule@gmail.com',
    'version': '0.1',  # modify as time passes
    'install_requires': ['nose'], # modify with needs
    'packages': ['NAME'], # modify
    'scripts': [], # modify
    'name': 'Diary of the Void'  
]

setup(**config)

from os.path import join, dirname
from setuptools import setup, find_packages

__version__ = open(join(dirname(__file__), 'smackbot/VERSION')).read().strip()

install_requires = (
    'requests>=2.4.0',
    'websocket-client>=0.22.0',
    'slacker>=0.9.50',
    'six>=1.10.0'
)  # yapf: disable

excludes = (
    '*test*',
    '*local_settings*',
)  # yapf: disable

setup(name='smackbot',
      version=__version__,
      license='MIT',
      description='A simple smack (read: chat) bot for Slack',
      author='Skyler Lewis and Contributors',
      author_email='sblnog@gmail.com',
      url='http://github.com/alairock/smackbot',
      platforms=['Any'],
      packages=find_packages(exclude=excludes),
      install_requires=install_requires,
      classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'])

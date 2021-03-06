from distutils.core import setup
import os.path

setup(
  name = 'siraben',         # How you named your package folder (MyLib)
  packages = ['siraben'],   # Chose the same as "name"
  version = '0.0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Show my name',   # Give a short description about your library
  long_description='plese read in: https://github.com/SiraArduino/siraben',
  author = 'Sira Benchapoowanon',                   # Type in your name
  author_email = 'sira.programmer@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/SiraArduino/siraben',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/SiraArduino/siraben/archive/0.0.3.zip',    # I explain this later on
  keywords = ['siraben', 'Sira', 'THAILAND', 'Benchapoowanon'],   # Keywords that define your package best
  install_requires=[
          'siraben',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)

import setuptools
from setuptools import setup

setup(name='vadaszApp',
      version='0.2',
      description='Practicing app for the Hunter Exam ',
      url='http://github.com/fecjanky/vadaszApp',
      author='Ferenc Janky',
      author_email='fecjanky@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=[
          'opencv-python',
          'Pillow'
      ],
      entry_points={  # Optional
          'console_scripts': [
              'vadaszApp=vadaszApp:main',
          ],
      },
      zip_safe=False)

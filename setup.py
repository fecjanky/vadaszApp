from setuptools import setup

setup(name='vadaszApp',
      version='0.1',
      description='Practicing app for the Hunter Exam ',
      url='http://github.com/fecjanky/vadaszApp',
      author='Ferenc Janky',
      author_email='fecjanky@gmail.com',
      license='MIT',
      packages=['vadaszApp'],
      install_requires=[
          'opencv-python',
          'Pillow'
      ],
      zip_safe=False)

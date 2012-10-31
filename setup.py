from setuptools import setup

version = '0.3'

setup(name='pynsq',
      version=version,
      description="a Python module for NSQ",
      keywords='python nsq',
      author='Matt Reiferson',
      author_email='snakes@gmail.com',
      url='http://github.com/bitly/pynsq',
      download_url='https://github.com/downloads/bitly/pynsq/pynsq-%s.tar.gz' % version,
      packages=['nsq'],
      requires=['tornado'],
      include_package_data=True,
      zip_safe=True,
      )

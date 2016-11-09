from setuptools import setup
from setuptools import find_packages

setup(
    name='tomspy3utils',
    version='0.0.1',
    description='Tom\'s python3 functions',
    url='https://github.com/TomHarrop/py3_utils',
    author='Tom Harrop',
    author_email='twharrop@gmail.com',
    license='GPL-3',
    packages=find_packages(),
    install_requires=[
        'datetime',
        'argparse>=1.1'
    ],
    zip_safe=False)

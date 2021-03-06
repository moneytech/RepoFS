import os

from setuptools import setup, find_packages
from distutils.extension import Extension

from subprocess import call

def get_long_desc():
    with open("README.md", "r") as readme:
        desc = readme.read()

    return desc


def setup_package():
    setup(
        name='repofs',
        version='0.2.4',
        description='File system view of git repositories',
        long_description=get_long_desc(),
        url='https://github.com/AUEB-BALab/RepoFS',
        license='Apache Software License',
        packages=find_packages(),
        data_files=[('man/man1', ['repofs.1'])],
        install_requires=['fusepy', 'pygit2==0.24.2'],
        entry_points = {
            'console_scripts': [
                'repofs=repofs.__main__:main',
            ],
        },
    )

if __name__ == '__main__':
    setup_package()

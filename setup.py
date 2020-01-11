from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    authoer='Anton D-KO',
    author_email='homedyachenko@gmail.com',
    description='A Utility for backing up PostgreSQL databases.',
    long_description=longs_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AntonD-KO/pgbackup',
    packages=find_packages('src')
)

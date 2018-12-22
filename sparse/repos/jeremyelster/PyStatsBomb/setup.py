# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='StatsBombPy',
    version='0.1.0',
    description='Write Python Client to Grab StatsBomb Data',
    long_description=readme,
    author='Jeremy Elster',
    author_email='jeremy.elster@gmail.com',
    url='https://github.com/',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

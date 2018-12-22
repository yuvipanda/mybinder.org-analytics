from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='timeperiod',
    version='0.2.1',
    packages=find_packages(),
    description='Simple date parser',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    include_package_data=True,
)

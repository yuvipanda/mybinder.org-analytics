from setuptools import setup, find_packages


# Import ``__version__`` variable
exec(open('mustaching/_version.py').read())

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='mustaching',
    version=__version__,
    author='Alex Raichev',
    url='https://github.com/araichev/mustaching',
    description='A Python 3.4+ package for Mr. Money Mustaching',
    long_description=readme,
    license=license,
    install_requires=[
        'pandas>=0.19',
        'python-highcharts>=0.3.1',
        'colorlover>=0.2.1',
    ],
    packages=find_packages(exclude=('tests', 'docs')),
)


from setuptools import setup, find_packages
from os import path

this_dir = path.abspath(path.dirname(__file__))
with open(path.join(this_dir, 'README.MD',), encoding='utf-8') as f:
    long_description = ''.join(f.readlines())

setup(
    name='dna_analyser_ibp',
    version='0.5.1',
    description='Tool for creating palindrome and G4hunter analysis on API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Patrik Kaura',
    author_email='patrikkaura@gmail.com',
    keywords='dna,ibp,quadruplex,g4hunter',
    license='GPLv3',
    url='https://github.com/PatrikKaura/DNA_analyser_IBP',
    packages=find_packages(),
    install_requires=['requests', 'pandas', 'tqdm'],
    classifiers=[
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
    zip_safe=False,
)

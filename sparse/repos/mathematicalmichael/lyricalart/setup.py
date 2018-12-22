#!/usr/bin/env python
# Copyright (C) 2018 Michael Pilosov

# Michael Pilosov 11/07/2018

'''
'''
try:
  from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='songsim',
      version='0.1.1',
      description='Consistent Bayesian Inversion',
      author='Michael Pilosov',
      author_email='mpilosov@gmail.com',
      license='MIT',
      packages=[],
      install_requires=['matplotlib', 'scipy', 'numpy',
          'ipykernel', 'ipywidgets', 'lyricwikia'] 
)


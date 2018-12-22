# -*- coding: utf-8 -*-

import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyelectrica",
    version="1.1.2",
    author="Isai Aragón",
    author_email="isaix25@gmail.com",
    description="Módulo PyElectrica, útil para resolver problemas específicos \
    de máquinas y circuitos eléctricos en la Ingeniería Eléctrica",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/x1sa1/PyElectrica",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Natural Language :: Spanish",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
    ],
)

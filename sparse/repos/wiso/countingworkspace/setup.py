import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="countingworkspace",
    version="0.0.3",
    author="Ruggero Turra",
    author_email="ruggero.turra@cern.ch",
    description="Simple builder for counting experiment RooFit workspace",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wiso/countingworkspace",
    packages=setuptools.find_packages(),
    install_requires=['numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
    ],
)

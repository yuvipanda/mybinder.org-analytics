from setuptools import setup

setup(name="ntnu.kt",
      version="0.0.8",
      description="Standard library for NTNU Konstruksjonsteknikk",
      url="https://github.com/ntnu-kt/ntnu.kt",
      author="Teodor Heggelund",
      author_email="teodor.heggelund@gmail.com",
      license="MIT",
      # List all packages; "All directories with __init__.py files"
      packages=["ntnu.kt", "ntnu.kt.course", "ntnu.kt.course.tkt4116"],
      zip_safe=False
      )

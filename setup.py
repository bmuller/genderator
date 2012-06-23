#!/usr/bin/env python
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

setup(
    name="genderator",
    version="0.1",
    description="Get gender from first name.  Uses gender.c file.",
    author="Brian Muller",
    author_email="bamuller@gmail.com",
    license="GPLv3",
    url="http://github.com/bmuller/genderator",
    packages=["genderator"],
    package_data={'genderator': ['data/nam_dict.txt']}
    )

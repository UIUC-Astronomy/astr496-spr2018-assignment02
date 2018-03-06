#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'numpy>=1.13.0',
    'h5py>=2.7.1',
    'matplotlib>=2.0.0'
]

setup_requirements = [
]

test_requirements = [
]

setup(
    name='nbody_code',
    version='0.1.0',
    description="Assignment 2 for ASTR-496 Spring 2018",
    long_description=readme + '\n\n',
    author="Your Name Here",
    author_email='youremail@illinois.edu',
    url='https://github.com/UIUC-Astronomy/astr496-spring2018-assignment02',
    packages=find_packages(include=['nbody_code']),
    entry_points={
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)

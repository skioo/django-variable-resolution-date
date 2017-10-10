#!/usr/bin/env python
from setuptools import setup

setup(
    name='django-variable-resolution-date',
    version='0.1.5',
    description='A django field that can represent either a year, or a year and a month, or a full calendar date',
    long_description='',
    author='Nicholas Wolff',
    author_email='nwolff@gmail.com',
    url='https://github.com/skioo/django-variable-resolution-date',
    download_url='https://pypi.python.org/pypi/django-tombstones',
    packages=[
        'variable_resolution_date',
    ],
    install_requires=[
        'Django>=1.10',
    ],
    licence='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

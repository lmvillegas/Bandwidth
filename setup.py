# -*- coding: utf-8 -*-

# Learn more: https://github.com/lmvillegas/Bandwidth/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Bandwidth',
    version='0.1.0',
    description='Medir ancho de banda',
    long_description=readme,
    author='Luis Villegas',
    author_email='lvillegas@sti.com.ve',
    url='https://github.com/lmvillegas/Bandwidth',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
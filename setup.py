# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='jamulizer',
    version='0.1.0',
    description='MIDI Analysis Visualization Tool',
    long_description=readme,
    author='Chris J Arges',
    author_email='christopherarges@gmail.com',
    url='https://github.com/arges/jamulizer',
    license=license,
    packages=find_packages(exclude=('test')),
    entry_points={
        'jamulizer' : [
            'jamulizer=jamulizer:__main__'
        ]
    },
)


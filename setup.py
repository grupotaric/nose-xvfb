# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requires = ['nose', 'xvfbwrapper']

setup(
    name='nose-xvfb',
    description='Virtual display nose plugin through Xvfb',
    version='0.11',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
        "Framework :: nose",
    ],
    entry_points={'nose.plugins.0.10': ['nosexvfb = nosexvfb:Xvfb']},
    install_requires=requires,
    packages=find_packages(),
    url='http://www.taric.es',
    author='Taric S.A.',
    author_email='',
)

# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requires = ['nose', 'xvfbwrapper==0.2.9']

setup(
    name='nose-xvfb',
    description='Virtual display nose plugin through Xvfb',
    version='0.13.1',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
    ],
    entry_points={'nose.plugins.0.10': ['nosexvfb = nosexvfb:Xvfb']},
    install_requires=requires,
    packages=find_packages(),
    url='https://github.com/grupotaric/nose-xvfb',
    author='Javier Santacruz',
    author_email='javier.santacruz.lc@gmail.com',
    keywords=['testing', 'nose', 'xvfb', 'x.org']
)

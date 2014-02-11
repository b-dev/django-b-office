#!/usr/bin/env python
"""
Installation script:

To release a new version to PyPi:
- Change te version below
- Run: python setup.py sdist upload
"""

from setuptools import setup, find_packages

setup(name='django-b-office',
      version="0.1",
      url='git@github.com:b-dev/django-b-office.git',
      author="Marco Minutoli",
      author_email="info@marcominutoli.it",
      description="A small django app for small office",
      long_description=open('README.rst').read(),
      keywords="office, invoice, Django, domain-driven",
      license='BSD',
      packages=find_packages(),
      install_requires=[],
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: Unix',
                   'Programming Language :: Python']
      )

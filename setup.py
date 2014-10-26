from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-feedback',
    version=version,
    description="Feedback Module for Data and Feature Requests",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Maulik R Kamdar',
    author_email='kamdarmax@gmail.com',
    url='www.maulik-kamdar.com',
    license='Creative Commons',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.feedback'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[

    ],
    entry_points='''
        [ckan.plugins]
        feedback=ckanext.feedback.plugin:FeedbackPlugin
    ''',
)

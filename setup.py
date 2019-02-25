#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''Generate the VCBSIG website'''


setup(
    name='vcbsig',
    version='0.1.0.0',
    author='Bernie Pope',
    author_email='bjpope@unimelb.edu.au',
    packages=['vcbsig'],
    package_dir={'vcbsig': 'vcbsig'},
    entry_points={
        'console_scripts': ['vcbsig = vcbsig.main:main']
    },
    url='https://github.com/bjpop/vcbsig',
    license='LICENSE',
    description=('Generate the VCBSIG website'),
    long_description=(LONG_DESCRIPTION),
    install_requires=["jinja2==2.9.6", "pyyaml"],
)

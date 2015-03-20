import sys
from setuptools import setup

install_requires = ['distribute']
if sys.version_info[0] == 2:
    install_requires.append('suds')
else:
    install_requires.append('suds-jurko')

setup(
    name='pycontrol',
    description='Library for F5 iControl API',
    long_description="""pyControl is a Python-based library that integrates
                        with F5's BIG-IP iControl management API.""",
    version='2.1',
    license='GPL',
    author='Matt Cauthorn',
    author_email='mcauthorn@gmail.com',
    url='https://github.com/mcauthorn/pycontrol',
    keywords='iControl F5 API',
    #py_modules=['pycontrol'],
    packages=['pycontrol',],
    install_requires=install_requires,
    platforms='any',
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)

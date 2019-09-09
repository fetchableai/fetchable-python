
import os
from setuptools import setup, find_packages

from fetchable.__version__ import __name__, __version__, __description__, __url__
from fetchable.__version__ import __author__, __author_email__, __license__

__url__ = ''
setup(name=__name__,
    version=__version__,
    description=__description__,
    project_urls={
        'Source': 'https://github.com/fetchableai/fetchable-python',
        'Issue tracker': 'https://github.com/fetchableai/fetchable-python/issues',
        'Company': 'https://fetchable.ai'
    },
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    packages=find_packages(exclude=['examples*']),
    long_description=open('README.rst', mode="r").read(),
    long_description_content_type='text/x-rst',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries '
    ]
)

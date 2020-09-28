#!/usr/bin/env python3

import setuptools
from setuptools import find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

__author__ = 'DeepMind, Chace Ashcraft'
__email__ = 'chace.ashcraft@jhuapl.edu'
__version__ = '0.0.0dev'


setuptools.setup(
    name='ai_safety_gridworlds',
    version=__version__,

    description='Fork of ai-safety-gridworlds repository by DeepMind',
    long_description=long_description,

    url='https://github.com/ChaceAshcraft/ai-safety-gridworlds/',

    author=__author__,
    author_email=__email__,

    license='Apache License 2.0',

    python_requires='>=3',
    packages=find_packages(),

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='deep-learning',

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['numpy',
                      'pycolab',
                      'absl-py'
                      ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={},

    zip_safe=False
)

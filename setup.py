# coding: utf-8

"""
    NEMO API v2
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "nemo-api"
VERSION = "2.0.0"
REQUIRES = [
    "urllib3 >= 1.26", 
    "six >= 1.10",
    "certifi",
    "python_dateutil",
    "aiohttp==3.7.4.post0",
    "ujson==4.3.0",
]
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name=NAME,
    author='NEMO Platform',
    author_email='tech@nemoverse.io',
    description='NEMOVERSE-API-SDK PyPI (Python Package Index) Package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/nemoverse/nemo_wallet_api_python',
    project_urls={
        'Documentation': 'https://gitlab.com/nemoverse/nemo_wallet_api_python',
        'Bug Reports':
        'https://gitlab.com/nemoverse/nemo_wallet_api_python/-/issues',
        'Source Code': 'https://gitlab.com/nemoverse/nemo_wallet_api_python'
    },
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src', exclude=["test", "tests"]),
    keywords='nemo platform, pypi, package, nemo api',
    include_package_data=True,
    python_requires='>=3.9',
    extras_require={
        'dev': ['check-manifest'],
    },
    entry_points= {
        'console_scripts': ['nemoverse-cli=nemo_api.cli.main:main']
    },
    install_requires=REQUIRES
)
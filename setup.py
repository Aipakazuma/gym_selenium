import os
from setuptools import setup, find_packages


# Package meta-data.
NAME = 'gym_selenium'
DESCRIPTION = ''
AUTHOR = 'aipa'
EMAIL = ''
URL = ''

# What packages are required for this module to be executed?
REQUIRED = [
    'gym',
    'numpy'
    'selenium',
    'chromedriver-binary'
]

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Load the package's __version__.py module as a dictionary.
about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    install_requires=REQUIRED,
    include_package_data=True,
    dependency_links=[],
    license='',
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)

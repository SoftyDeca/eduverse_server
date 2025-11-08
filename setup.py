import sys
from setuptools import setup, find_packages

NAME = "eduverse_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="EduVerse",
    author_email="",
    url="",
    keywords=["OpenAPI", "EduVerse"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['eduverse_server=eduverse_server.__main__:main']},
    long_description="""\
    API платформы EduVerse. Авторы: команда 5 
    """
)


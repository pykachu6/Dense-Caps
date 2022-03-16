import setuptools
from setuptools import find_packages, setup

setuptools.setup(
    name='crystpredict',packages=find_packages(where="environment.yml")
    )
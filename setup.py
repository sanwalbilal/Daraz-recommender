from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="DARAZ RECOMMENDER",
    version="0.1",
    author="Sanwal bilal",
    packages=find_packages(),
    install_requires = requirements,
)
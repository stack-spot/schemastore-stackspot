from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="stackspot_store",
    version="0.1.8",
    description="",
    long_description=long_description,
    url="https://github.com/stack-spot/schemastore-stackspot",
    license="MIT",
    author="andrecintra",
    author_email="andre.cintra@zup.com.br",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
)

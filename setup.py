from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="Storm",
    version="1.0.0",
    description="Command-line interface for load testing api's, server checks, and async requests",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/teaglebuilt/Storm",
    author="Dillan Teagle",
    author_email="dillan.teagle.va@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    py_modules=["storm"],
    include_package_data=True,
    install_requires=[
        'Click', 'requests'
    ],
    entry_points={
        "console_scripts": ['storm=src.cli:main'],
    },
)

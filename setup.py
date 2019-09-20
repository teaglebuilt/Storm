from setuptools import setup



setup(
    name="Storm",
    version="1.0",
    py_modules=["storm"],
    install_requires=[
        'Click', 'requests'
    ],
    entry_points={
        "console_scripts": ['storm=src.cli:main'],
    },
)

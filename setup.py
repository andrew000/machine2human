from setuptools import setup

import m2h

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='machine2human',
    version=m2h.__version__,
    packages=['m2h'],
    url='https://github.com/andrew000/machine2human',
    license='MIT License',
    author='AndrewKing',
    python_requires='>=3.6',
    description='Make machine more friendly to you! Convert seconds to a human string and back!',
    long_description=long_description,
    long_description_content_type="text/markdown",
)

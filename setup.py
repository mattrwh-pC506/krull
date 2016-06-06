from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='krull',

    version='0.0.6',

    description='This is a lightweight microframework for building restful APIs',
    long_description=long_description,

    url='https://github.com/mattrwh/krull',

    author='Matthew Whitt',
    author_email='mwhitt.w@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='rest, api, web framework, micro-framework',

    packages=find_packages(),
    install_requires=[],

    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
)

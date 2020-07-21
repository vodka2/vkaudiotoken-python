from setuptools import setup, find_packages
from os import path

from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vkaudiotoken',
    version='0.5.1',
    description='Code that obtains VK tokens that work for VK audio API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vodka2/vkaudiotoken-python',
    author='vodka2',
    author_email='vodka2vodka@rambler.ru',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='vk vkontakte audio music',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    install_requires=['requests'],
    project_urls={
        'Bug Reports': 'https://github.com/vodka2/vkaudiotoken-python/issues',
        'Source': 'https://github.com/vodka2/vkaudiotoken-python',
    },
)

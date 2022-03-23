import codecs
from os import path
from setuptools import setup


setup(
    name='wnb',
    version='0.0.1',
    description='Python library for the implementations of weighted Naive Bayes (WNB) classifiers.',
    keywords=['python', 'bayes', 'naivebayes', 'classifier', 'probabilistic'],
    author='Mehdi Samsami',
    author_email='mehdisamsami@live.com',
    url='https://github.com/msamsami/weighted-naive-bayes',
    long_description=codecs.open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=['wnb'],
    classifiers=[
        'Topic :: Probabilistic Classification',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires=">=3.4",
    install_requires=['pandas==1.4.1', 'scipy==1.8.0'],
    extras_require={},
)

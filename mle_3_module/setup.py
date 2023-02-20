import codecs
import os

from setuptools import find_packages, setup

setup(
    name="housing_pkg",
    version="0.0.1",
    author="Rama Krishna",
    description="Ingest data, train and score models",
    long_description="Make various models to predict house price, score each model and log all the details",
    packages=find_packages(),
)

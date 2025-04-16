from setuptools import setup, find_packages

setup(
    name="ithinkitmlops",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas", "numpy", "scikit-learn"  # add other required packages
    ]
)

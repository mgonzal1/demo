from setuptools import setup, find_packages

setup(
    name="math",
    version="0.1.0",
    packages=find_packages(where="mymath"),
    package_dir={"": "mymath"},
    install_requires=[],
    python_requires=">=3.10",
)

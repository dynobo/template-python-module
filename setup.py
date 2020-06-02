# Standard
from setuptools import setup, find_packages
import myapp.configs as configs

with open("README.md") as f:
    readme = f.read()

setup(
    name=configs.MODULE["name"],
    version=configs.MODULE["version"],
    description="My template module",
    keywords="template blueprint",
    long_description_content_type="text/markdown",
    long_description=readme,
    author=configs.MODULE["author"],
    author_email=configs.MODULE["email"],
    url=configs.MODULE["repo"],
    license="MIT License",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    entry_points={"console_scripts": ["myapp=myapp.__main__:run"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: POSIX :: Linux",
    ],
)

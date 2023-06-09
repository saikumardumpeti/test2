from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sai/__init__.py
from sai import __version__ as version

setup(
	name="sai",
	version=version,
	description="details",
	author="sai",
	author_email="sai@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

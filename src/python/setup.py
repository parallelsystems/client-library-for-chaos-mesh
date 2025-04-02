from glob import iglob
from pathlib import Path

from setuptools import find_packages
from setuptools import setup

version_file = "version.txt"

this_directory = Path(__file__).parent
long_description = (this_directory / "../../README.md").read_text()


def get_version():
    with open(version_file) as f:
        return f.read().strip()


def get_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(name='client-library-for-chaos-mesh',
      version=get_version(),
      description='A client to create experiments in ChaosMesh',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Vishrant Gupta',
      author_email='vishrant.gupta@gmail.com',
      packages=find_packages(),
      url='https://github.com/vishrantgupta/client-library-for-chaos-mesh',
      include_package_data=True,
      install_requires=get_requirements(),
      platform='any',
      data_files=[
          ('version.txt', iglob('version.txt', recursive=True)),
          ('NOTICE', iglob('NOTICE', recursive=True)),
          ('NOTICE', iglob('NOTICE', recursive=True)),
      ],
      zip_safe=False)

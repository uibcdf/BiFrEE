from setuptools import find_packages
from numpy.distutils.core import setup
from numpy.distutils.extension import Extension

extensions_list=[]

setup(
    name='openmmgbsa',
    version='0.0.1',
    author='UIBCDF Lab and contributors',
    author_email='uibcdf@gmail.com',
    package_dir={'openmmgbsa': 'openmmgbsa'},
    packages=find_packages(),
    ext_modules=extensions_list,
    package_data={'openmmgbsa': []},
    scripts=[],
    url='http://uibcdf.org',
    download_url ='https://github.com/uibcdf/OpenMMGBSA',
    license='MIT',
    description="---",
    long_description="---",
)


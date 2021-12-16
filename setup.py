from setuptools import (setup, find_packages)
# from distutils.util import convert_path
#
# main_ns = {}
# ver_path = convert_path('version.py')
# with open(ver_path) as ver_file:
#     exec(ver_file.read(), main_ns)

from mod1 import __version__

setup(
    name='SimplePyPkg',
    version=__version__,
    packages=find_packages(include=['mod1']),
    install_requires=['pandas'],
    # package_data={'mod1': ['data/*']},
    url='https://github.com/HuangRicky/SimplePyPkg',
    license='GPLv3',
    author='Ruokun Huang',
    author_email='hruokun.2008@gmail.com',
    description='Sample Python Package Skeleton'
)

# to install, use your prompt (anaconda prompt) to:
# either pip install the wheel (if you compile)
# or cd into this directory, then pip install .    (note: include the DOT!)
# to compile a wheel, cd into this dir, then
# python setup.py bdist_wheel

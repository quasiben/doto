import sys

from distutils.core import setup

import versioneer


versioneer.versionfile_source = 'doto/_version.py'
versioneer.versionfile_build = 'doto/_version.py'
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'doto-'

cmdclass = versioneer.get_cmdclass()

setup(
    name = 'doto',
    version = versioneer.get_version(),
    description='Python Interface to Digital Ocean',
    author = 'Benjamin Zaitlen',
    packages = ['doto'],
    install_requires=['requests>=2.0.1',],
    package_data={'doto':['dotorc']},
)
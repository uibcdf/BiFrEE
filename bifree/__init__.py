"""
BiFrEE
This must be a short description of the project
"""

# versioningit
from ._version import __version__

__documentation_web__ = 'https://www.uibcdf.org/BiFrEE'
__github_web__ = 'https://github.com/uibcdf/BiFrEE'
__github_issues_web__ = __github_web__ + '/issues'

from . import config
from ._pyunitwizard import puw as pyunitwizard

from . import systems

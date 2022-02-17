"""
BiFrEE
Binding Free Energy Estimator
"""

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

__documentation_web__ = 'https://www.uibcdf.org/BiFrEE'
__github_web__ = 'https://github.com/uibcdf/BiFrEE'
__github_issues_web__ = __github_web__ + '/issues'

from ._pyunitwizard import puw as puw

from .test import greetings


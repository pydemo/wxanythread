
from distutils.core import setup

wxAnyThread = {}
try:
    execfile("wxAnyThread/__init__.py",wxAnyThread)
except ImportError:
    pass

NAME = "wxAnyThread"
DESCRIPTION = "Allow wxPython object methods to be called from any thread."
AUTHOR = "Ryan Kelly"
AUTHOR_EMAIL = "ryan@rfk.id.au"
URL = "http://pypi.python.org/pypi/wxAnyThread/"
LICENSE = "MIT"
KEYWORDS = "wxPython threading"

PACKAGES = ["wxAnyThread"]

setup(name=NAME,
      version=wxAnyThread["__version__"],
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      description=DESCRIPTION,
      long_description=wxAnyThread["__doc__"],
      license=LICENSE,
      keywords=KEYWORDS,
      packages=PACKAGES,
     )


from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=['racing'],
	package_dir={'': 'api'}
)

setup(**setup_args)
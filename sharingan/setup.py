from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["./intensity_transforms.pyx", "./change_color_space.py"])
)
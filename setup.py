from setuptools import find_packages, setup
from setuptools.extension import Extension

from Cython.Build import cythonize

extensions = [
    Extension(
        'aabb',
        ['aabb.pyx',
                 'aabb_wrapper.cpp'],
        # libraries=['cgal'],
        include_dirs=['.',
                      # add path to cgal, then boost include dirs
                    ],
        language='c++',
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp']
    )
]

setup(
    name='aabb',
    packages=find_packages(),
    ext_modules=cythonize(extensions),
    zip_safe=False
)

from setuptools import setup, Extension
import pybind11

setup(
    name='sum_array',
    ext_modules=[
        Extension(
            'sum_array',
            sources=['sum_array.cc'],
            include_dirs=[pybind11.get_include()],
            language='c++',
            extra_compile_args=["-std=c++11"],
        )
    ],
    zip_safe=False,
)

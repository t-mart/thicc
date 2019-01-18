from setuptools import setup, find_packages

setup(
    name='fw',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/t-mart/fw',
    license='MIT License',
    author='tmartin',
    author_email='tim@timmart.in',
    description='Convert characters to their fullwidth representation',
    entry_points={
        'console_scripts': [
            'fw = fw:main',
        ],
    },
)

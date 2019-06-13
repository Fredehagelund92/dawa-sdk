
from setuptools import find_packages, setup

try:
    long_description = open('README.md').read()
except IOError:
    long_description = ""

setup(
    name='dawa-sdk',
    version='0.0.2',
    description='Python Dawa API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Fredehagelund92/dawa-python',
    author='Frederik Hagelund',
    author_email='frederik.hagelund@gmail.com',
    license='GPL',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['dawa', 'api', 'python'],
    packages=find_packages(exclude=('tests')),
    install_requires=['requests'],
    tests_require=['pytest'],
)

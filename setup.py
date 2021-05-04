
from setuptools import find_packages, setup

try:
    long_description = open('README.md').read()
except IOError:
    long_description = ""

setup(
    name='dawa-sdk',
    version='0.2.4',
    description='Python Dawa API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Fredehagelund92/dawa-sdk',
    author='Frederik Hagelund',
    author_email='frederik.hagelund@gmail.com',
    license='GPL',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['dawa', 'api', 'python'],
    packages=find_packages(exclude=('tests')),
    install_requires=['requests==2.25.1'],
    tests_require=['pytest==6.2.1'],
)

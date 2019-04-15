try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    long_description = open('README.md').read()
except IOError:
    long_description = ""

setup(
    name='dawa-python',
    version='1.0.13',
    description='Python Dawa API',
    long_description=long_description,
    url='https://github.com/Fredehagelund92/dawa-python',
    author='Frederik Hagelund',
    author_email='frederik.hagelund@gmail.com',
    license='GPL',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.5',
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords="dawa data api python",
    packages=[],
    install_requires=['requests']
)

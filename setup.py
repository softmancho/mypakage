from setuptools import setup, find_packages

setup(

    name = 'mypakage',
    version = '0,1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/softmancho/mypakage',
    author='Justice Oyemike',
    author_email='justyaso2@gmil.com'
    
)
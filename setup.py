from setuptools import setup, find_packages

setup(
    name='ddosxd-api',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'requests'
    ],
    url='https://github.com/dudosxd/ddosxd-api',
    license='MIT',
    author='ddosxd',
    author_email='ddosxd@proton.me',
    description='Python library for ddosxd.ru API'
)

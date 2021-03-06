from setuptools import setup

setup(
    name='autoresponse',
    version='0.3.1',
    description=('A Python package for automatically generating'
                 ' Response objects for scrapy.http.Request objects'),
    url='https://github.com/paulproteus/autoresponse',
    packages=['autoresponse'],
    license='Apache License 2.0',
    long_description=open('README').read(),
    install_requires=[
        'scrapy',
        ],
)


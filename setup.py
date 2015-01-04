from setuptools import setup

setup(
    name='autoresponse',
    version='0.3.1',
    packages=['autoresponse'],
    license='Apache License 2.0',
    long_description=open('README').read(),
    description='Package for automatically generating Response objects for scrapy.http.Request objects',
    install_requires=[
        'scrapy',
        ],
)


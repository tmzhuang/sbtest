from setuptools import setup

setup(name='sbtest',
        version='0.1',
        description='A collection of modules to facilitate the testing of sbengine',
        url='',
        author='Tianming Zhuang',
        author_email='tzhuang@cranksoftware.com',
        packages=['sbtest'],
        test_suite='nose.collector',
        tests_require=['nose'],
        zip_safe=False)

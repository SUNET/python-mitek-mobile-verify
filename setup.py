from setuptools import setup

setup(
    name='mitek_mobile_verify',
    version='0.0.1b0',
    packages=['mitek_mobile_verify'],
    install_requires=[
        'zeep==0.24.0'
    ],
    test_suite='nose2.collector.collector',
    tests_require=['nose2'],
    url='https://github.com/SUNET/python-mitek-mobile-verify',
    license='',
    author='Johan Lundberg',
    author_email='lundberg@sunet.se',
    description='Implementation of Mitek SOAP service for drivers license verification'
)

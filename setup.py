from distutils.core import setup

setup(
    name='mitek_mobile_verify',
    version='0.1b0',
    packages=[
        'zeep==0.24.0'
    ],
    url='https://github.com/SUNET/python-mitek-mobile-verify',
    license='',
    author='Johan Lundberg',
    author_email='lundberg@sunet.se',
    description='Implementation of Mitek SOAP service for drivers license verification'
)

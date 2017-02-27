from setuptools import setup, find_packages

setup(
    name='mitek_mobile_verify',
    version='0.0.2',
    package_dir={'':'mitek_mobile_verify'},
    packages=find_packages('mitek_mobile_verify', exclude=['tests']),
    install_requires=[
        'zeep==1.0.0'
    ],
    test_suite='nose2.collector.collector',
    tests_require=['nose2'],
    url='https://github.com/SUNET/python-mitek-mobile-verify',
    license='2-clause BSD license',
    zip_safe=False,
    author='Johan Lundberg',
    author_email='lundberg@sunet.se',
    description='Implementation of Mitek SOAP service for drivers license verification'
)

import setuptools
import json

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ringcentral_engage_digital_source_sdk",
    version="0.0.1",
    author="Drake Zhao @ RingCentral",
    author_email="drake.zhao@ringcentral.com",
    description="RingCentral engage digital channel SDK Framework for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ringcentral/engage-digital-source-sdk-python",
    packages=setuptools.find_packages(),
    keywords=['ringcentral', 'SDK', 'framework', 'Engage Digital'],
    install_requires=[i.strip() for i in open('requirements.txt').readlines()],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['rces=ringcentral_engage_digital_source_sdk.rces:main'],
    }
)
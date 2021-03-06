#!usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
try:
    from pipenv.project import Project
    from pipenv.utils import convert_deps_to_pip

    pfile = Project().parsed_pipfile
    requirements = convert_deps_to_pip(pfile['packages'], r=False)
    test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)
except ImportError:
    # get the requirements from the requirements.txt
    requirements = [line.strip()
                    for line in open('requirements.txt').readlines()
                    if line.strip() and not line.startswith('#')]
    # get the test requirements from the test_requirements.txt
    test_requirements = [line.strip()
                         for line in
                         open('dev-requirements.txt').readlines()
                         if line.strip() and not line.startswith('#')]

readme = open('README.md').read()
history = open('HISTORY.md').read().replace('.. :changelog:', '')
version = open('.VERSION').read()


setup(
    name='''azure-sdk-security-sample''',
    version=version,
    description='''Project energy labeling accounts and landing zone based on findings of Microsoft Defender for Cloud in Azure cloud.''',
    long_description=readme + '\n\n' + history,
    author='''''',
    author_email='''''',
    url='''https://github.com/luander/azure-sdk-security-sample.git''',
    packages=find_packages(where='.', exclude=('tests', 'hooks', '_CI*')),
    package_dir={'''azure-sdk-security-sample''':
                 '''azure-sdk-security-sample'''},
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    keywords='''azure-sdk-security-sample''',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        ],
    test_suite='tests',
    tests_require=test_requirements
)


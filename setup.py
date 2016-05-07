import os
from setuptools import setup

ROOT = os.path.abspath(os.path.dirname(__file__))

setup(
    name="django-expvar-cmdline",
    version="0.1.0",
    author="Anders Pearson",
    author_email="anders@columbia.edu",
    url="https://github.com/thraxil/django-expvar-cmdline",
    description="Django expvar endpoint cmdline plugin",
    long_description=open(os.path.join(ROOT, 'README.md')).read(),
    install_requires=['Django>=1.8', 'nose', 'six', 'django-expvar'],
    scripts=[],
    license="BSD",
    platforms=["any"],
    zip_safe=False,
    package_data = {'': ['*.*']},
    packages=['expvarcmdline'],
    test_suite='nose.collector',
)

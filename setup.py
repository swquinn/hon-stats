"""
    hon-stats
    ~~~~~

    A plugin for Hon that counts the number of words, pages, etc. in a project.
"""
import io
import re

from setuptools import setup, find_packages

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("hon_stats/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = [\'"](.*?)[\'"]', f.read(), re.M).group(1)

setup(
    name="hon_stats",
    version=version,
    url="https://github.com/swquinn/hon-stats",
    project_urls={
        "Documentation": "https://swquinn.github.io/hon-stats",
        "Code": "https://github.com/swquinn/hon-stats",
        "Issue tracker": "https://github.com/swquinn/hon-stats/issues",
    },
    license="MIT",
    author="Sean Quinn",
    maintainer="swquinn",
    description="Analyzes the rendered book and outputs statistics about it.",
    long_description=readme,
    packages=find_packages(exclude='tests/*'),
    include_package_data=True,
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
    install_requires=[
        'hon'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'hon.plugins': [
            'stats=hon_stats:HonStats'
        ]
    }
)

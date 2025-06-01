from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name='beets-rym-genres',
    version='1.0.0',
    description='Beets plugin to fetch genre data from Rate Your Music via Firebase',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='beets-rym-genres',
    author_email='',
    url='https://github.com/yourusername/beets-rym-genres',
    license='MIT',
    packages=find_packages(),
    package_data={
        '': ['data/*.json'],
    },
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.7',
    entry_points={
        'beets.plugins': [
            'rym_genres = beetsplug.rym_genres:RYMGenresPlugin',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
    ],
    keywords='beets plugin music genres rate-your-music rym tagging',
)
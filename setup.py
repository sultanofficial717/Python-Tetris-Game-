"""
Setup script for Python Tetris Game

This allows the project to be installed as a package:
    pip install -e .
    
Or distributed:
    python setup.py sdist bdist_wheel
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='python-tetris-game',
    version='1.0.0',
    author='Sultan Official',
    author_email='sultanofficial717@github.com',
    description='A professional, educational Tetris game implementation in Python with Pygame',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sultanofficial717/Python-Tetris-Game-',
    project_urls={
        'Bug Reports': 'https://github.com/sultanofficial717/Python-Tetris-Game-/issues',
        'Source': 'https://github.com/sultanofficial717/Python-Tetris-Game-',
        'Documentation': 'https://github.com/sultanofficial717/Python-Tetris-Game-/tree/main/docs',
    },
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment :: Puzzle Games',
        'Topic :: Education',
        'Topic :: Software Development :: Libraries :: pygame',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    keywords=[
        'tetris', 'game', 'pygame', 'python', 'educational',
        'game-development', 'puzzle', 'arcade', 'tutorial',
        'learning', 'oop', 'beginner-friendly'
    ],
    python_requires='>=3.7',
    install_requires=[
        'pygame>=2.0.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'black>=21.0',
            'flake8>=3.9',
            'mypy>=0.910',
        ],
    },
    entry_points={
        'console_scripts': [
            'tetris=main:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

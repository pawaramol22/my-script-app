from setuptools import setup, find_packages

setup(
    name='myscriptsapp',  # Package name
    version='1.0.0',
    description='A Python package for automating CLI workflows',
    author='Amol Pawar',
    author_email='your_email@example.com',
    packages=find_packages(where='src'), # Find packages within 'src'
    package_dir={'': 'src'}, # Tell setuptools that packages are under 'src'
    install_requires=[  # List dependencies from requirements.txt
       # ...
    ],
    entry_points = {
        'console_scripts': [
            'myscriptsapp=myscriptsapp.main:main'  # Example command-line entry point
        ]
    },
    # Assuming you are using pytest for testing
    test_suite='tests',  # Point setup.py to your 'tests' directory 
)

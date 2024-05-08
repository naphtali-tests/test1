from setuptools import setup, find_packages

setup(
    name='my_package',
    version='1.0.0',
    description='A simple Python package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/my-python-project',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'requests==1.0',
        'numpy==1.3',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

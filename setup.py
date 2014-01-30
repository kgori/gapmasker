from distutils.core import setup

setup(name='gapmasker',
    version='1.0',
    description='Adds gaps to an alignment according to a template',
    author='Kevin Gori',
    author_email='kgori@ebi.ac.uk',
    url='',
    packages=['gapmasker', 
        'gapmasker.errors', 
        'gapmasker.readers', 
        'gapmasker.utils',
    ],
)
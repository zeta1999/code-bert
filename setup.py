from distutils.core import setup
from code_bert import __version__


setup(
name='CodeBERT',
version=__version__,
packages=['code_bert',],
entry_points = {
    'console_scripts': ['create_training_data=code_bert.cli.training_data_prep:main'],
},
license='Creative Commons Attribution-Noncommercial-Share Alike license',
)
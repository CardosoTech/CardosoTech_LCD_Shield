from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name 				= 'CardosoTech_LCD_Shield',
	  version 			= '0.1.0',
	  author			= ' ',
	  author_email		= ' ',
	  description		= 'Library to display images on the Nokia 5110/3110 LCD.',
	  license			= 'MIT',
	  url				= 'https://github.com/adafruit/CardosoTech_LCD_Shield/',
	  dependency_links	= ['https://github.com/adafruit/CardosoTech_Python_GPIO/tarball/master#egg=CardosoTech-GPIO-0.1.0'],
	  install_requires	= ['CardosoTech-GPIO>=0.1.0'],
	  packages 			= find_packages())

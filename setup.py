from setuptools import setup

setup(
	name = 'barcodegen',
	version = '0.1',
	
	description = 'A Python module generating barcode images',
	
	url = 'https://github.com/fizyk20/python-barcode',
	
	author = 'Bartłomiej Kamiński',
	author_email = 'fizyk20@gmail.com',
	
	license = 'GPLv3',
	
	classifiers = [
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4'
	],
	
	keywords = 'barcode',
	
	install_requires = ['pillow']
)
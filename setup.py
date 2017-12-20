#!/usr/bin/env python
#coding: utf-8

from setuptools import setup

setup(
	name = 'ahahahaha',
	version = '0.1',
	author = 'wph',
	author_email = 'wangpenghui@gene.ac',
	url = 'https://testupload.test',
	description = 'test how to submit a project to pypi',
	packages = ['uploadpy'],
	install_requires = [],
	entry_points = {
		'console_scripts':[
			'uploadpy = uploadpy:uploadpy',
			'pypy = uploadpy:pypy'
		]
	}
)

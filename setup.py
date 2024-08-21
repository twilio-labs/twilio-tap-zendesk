#!/usr/bin/env python

from setuptools import setup

setup(
      name='twilio-tap-zendesk',
      version='1.0.18',
      description='Singer.io tap for extracting data from the Zendesk API',
      author='Twilio',
      url='https://github.com/twilio-labs/twilio-tap-zendesk',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_zendesk'],
      install_requires=[
          'pipelinewise-singer-python==1.2.0',
          'zenpy==2.0.49',
          'requests==2.32.3',
      ],
      extras_require={
          'dev': [
              'ipdb',
              'pylint',
              'nose',
              'nose-watch',
          ]
      },
      entry_points='''
          [console_scripts]
          tap-zendesk=tap_zendesk:main
      ''',
      python_requires=">=3.8",
      packages=['tap_zendesk'],
      include_package_data=True,
)

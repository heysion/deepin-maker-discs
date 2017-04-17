from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='deepin-maker-discs',
      version=version,
      description="deepin build maker discs tools platform",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='deepin maker discs',
      author='heysion',
      author_email='heysion@deepin.com',
      url='deepin.org',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

from setuptools import setup, find_packages
import os

version = open(os.path.join("Products", "CMFContentPanels", "version.txt")).read().strip()

setup(name='Products.CMFContentPanels',
      version=version,
      description="CMFContentPanels is a plone portlets product to build composite pages",
      long_description=open(os.path.join("Products", "CMFContentPanels", "README.txt")).read().decode('UTF8').encode('ASCII', 'replace'),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone"
        ],
      keywords='plone web composite_pages CMFContentPanels',
      author='Erico Andrei',
      author_email='erico@simplesconsultoria.com.br',
      url='http://svn.plone.org/svn/collective/Products.CMFContentPanels/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-,
          'feedparser',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

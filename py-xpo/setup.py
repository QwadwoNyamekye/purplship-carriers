from setuptools import setup

setup(name='py-xpo',
      version='1.0-alpha',
      description='XPO Logistics Services Python Data domain library',
      url='https://github.com/PurplShip/purplship-carriers/tree/master/py-xpo',
      author='PurplShip',
      author_email='danielk.developer@gmail.com',
      license='MIT',
      packages=['pyxpo'],
      install_requires=[
            'attrs==18.2.0',
            'jstruct==1.0.0'
      ],
      dependency_links=[
            'https://git.io/purplship',
      ],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      zip_safe=False)

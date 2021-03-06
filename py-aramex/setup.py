from setuptools import setup

setup(name='py-aramex',
      version='1.0-alpha',
      description='Aramex Python Data domain library',
      url='https://github.com/PurplShip/purplship-carriers/tree/master/py-aramex',
      author='PurplShip',
      author_email='danielk.developer@gmail.com',
      license='MIT',
      packages=['pyaramex'],
      exclude=["schemas"],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      zip_safe=False)
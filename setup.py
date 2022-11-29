from setuptools import setup, find_packages


setup(
    name='terminalbreaker',
    packages=['terminalbreaker'],
    version='0.1.1',
    license='MIT',
    author="Ellicode",
    author_email='hello@ellicode.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'colorama==0.4.6',
      ],

)

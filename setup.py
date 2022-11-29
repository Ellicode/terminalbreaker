from setuptools import setup, find_packages


setup(
    name='terminalbreaker_py',
    version='0.1.8',
    license='MIT',
    author="Ellicode",
    author_email='ellicode22@gmail.com',
    packages=["terminalbreaker"],
    package_dir={'': 'src'},
    description="BREAK THE TERMINAL! Create panels, forms, dialogs and buttons into your Python CLI app!",
    url='https://github.com/Ellicode/terminalbreaker/blob/main/README.md',
    keywords='example project',
    install_requires=[
          'colorama==0.4.6',
      ],

)

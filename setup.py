from setuptools import setup, find_packages


setup(
    name='terminalbreaker',
    version='0.1.5',
    license='MIT',
    author="Ellicode",
    author_email='ellicode22@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    description="BREAK THE TERMINAL! Create panels, forms, dialogs and buttons into your Python CLI app!",
    url='https://github.com/Ellicode/terminalbreaker/blob/main/README.md',
    keywords='example project',
    install_requires=[
          'colorama==0.4.6',
      ],

)

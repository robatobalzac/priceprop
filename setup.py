from setuptools import setup, find_packages

setup(
    name='priceprop',
    version='1.0.3',
    description=(
        'Calibrate and simulate linear propagator models for the price '
        'impact of an extrinsic order flow.'
    ),
    long_description="""
        The models and methods are explained in:
	
            Patzelt, F. and Bouchaud, J-P.:
            Nonlinear price impact from linear models
            Journal of Statistical Mechanics (2017, in print)
            Preprint at arXiv:1706.04163
    """,
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3 :: 8",
        "Programming Language :: Python :: 3 :: 9",
        "Programming Language :: Python :: 3 :: 10",
        "Programming Language :: Python :: 3 :: 11"
    ],
    keywords=[
        'propagator', 'price impact', 'intra day', 'order flow', 
        'price return', 'Transient Impact Model', 'TIM', 
        'History Dependent Impact Model', 'HDIM'
    ],
    url='http://github.com/felixpatzelt/priceprop',
    download_url=(
      'https://github.com/felixpatzelt/priceprop/archive/1.0.3.tar.gz'
    ),
    author='Felix Patzelt',
    author_email='felix@neuro.uni-bremen.de',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24", 
        "scipy>=1.10", 
        "pandas>=2.0", 
        "scorr @ git+https://github.com/robatobalzac/scorr.git"
    ],
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
    extras_require={'dev': ['pytest>=8', 'tox>=4']}
)
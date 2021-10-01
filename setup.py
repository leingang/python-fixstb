from setuptools import setup

setup(
    name='fixstb',
    version='0.1.0',
    py_modules=['fixstb'],
    install_requires=[
        'Click','latex2mathml'
    ],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fixstb = fixstb:cli',
        ],
    },
)
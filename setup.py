from setuptools import setup

setup(
    name='yourscript',
    version='0.1.0',
    py_modules=['fixstb'],
    install_requires=[
        'Click','latex2mathml'
    ],
    entry_points={
        'console_scripts': [
            'fixstb = fixstb:cli',
        ],
    },
)
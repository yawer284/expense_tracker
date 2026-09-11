from setuptools import setup

setup(
    name="expense-tracker",
    version="0.1.0",
    py_modules=['main', 'storage', 'models'],
    entry_point={
        'console_scripts': [
            'expense-tracker = main : main'
        ],
    }, 
)
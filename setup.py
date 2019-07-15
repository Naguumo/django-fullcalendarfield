import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


setup(
    name='django-fullcalendarfield',
    version='0.0',
    packages=['fullcalendarfield'],
    description='A Model Friendly Implementation of FullCalendar using only JSON to save',
    long_description=README,
    author='Ishaan Bharal',
    author_email='ishbharal@gmail.com',
    url='https://github.com/Naguumo/django-fullcalendarfield',
    license='MIT',
    install_requires=[
        'Django>=2.2',
    ]
)
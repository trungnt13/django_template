from setuptools import setup, find_packages
from django_template import __version__

setup(
    name='{{ django_template }}',
    version=__version__,

    url='http://host/',
    author='TrungAnh',
    author_email='trungnt13@outlook.com',

    packages=find_packages(),
    include_package_data=True,
    scripts=['manage.py'],

    install_requires=(
        'django>1.7',
    )
)

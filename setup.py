from setuptools import setup, find_packages
from cybots import __version__

setup(
    name='{{ cybots }}',
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

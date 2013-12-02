from setuptools import setup, find_packages
import bootstrap_helpers
setup(name='django-test-views',
	version=bootstrap_helpers.__version__,
	packages = find_packages(),
	license='The MIT License',
	platforms=['OS Independent'],
	keywords='django, testing',
	author='Jon Bolt',
	author_email='jon@epicbagel.com',
	url="https://github.com/epicbagel/django-bootstrap-helpers",
)

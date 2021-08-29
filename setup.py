from setuptools import setup, find_packages

DEPENDENCIES = [
    'dash',
    'dash-bootstrap-components',
    'gunicorn'
]

with open("README.md", "r") as f:
    readme = f.read()


setup(
    name='pylance_dash_issue_demo',
    version='1.0.0',
    description='short description of the app',
    long_description=readme,
    author='Krzysztof Czarnecki',
    author_email='kjczarne@gmail.com',
    install_requires=DEPENDENCIES
)

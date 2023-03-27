from setuptools import setup, find_packages

def main():
    install_requires = ['requests']
    tests_require = ['pytest', 'pytest-timeout']
    dev_requires = ['tox']
    extras_require = {'test': tests_require, 'dev': dev_requires}
    setup(name='BoxSDK', version='2.0.0', description='[Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.', licence='Apache-2.0, http://www.apache.org/licenses/LICENSE-2.0', install_requires=install_requires, tests_require=tests_require, extras_require=extras_require, packages=find_packages(exclude=['docs', '*test*']))

if __name__ == '__main__':
    main()
from setuptools import setup, find_packages

def main():
    install_requires = ['requests']
    setup(name='OpenAPILibrary', version='1.0', install_requires=install_requires, packages=find_packages())

if __name__ == '__main__':
    main()
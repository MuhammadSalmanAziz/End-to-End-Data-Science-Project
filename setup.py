from setuptools import find_packages , setup
from typing import List

def get_requirements(file_path:str)->list[str]:
    '''
    This Function will return the List of Libraries in Requirements Text File
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    return requirements


setup(
    name="MLProject",
    version="0.0.1",
    author="Muhammad Salman Aziz",
    author_email="m.salmanaziz12@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements("requirements.txt"),
)

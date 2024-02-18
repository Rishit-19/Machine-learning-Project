from setuptools import setup,find_packages
from typing import List

hypen_e= "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirement
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hypen_e in requirements:
            requirements.remove(hypen_e)

    return requirements


setup(
    name= 'mlproject',
    version= '0.0.1',
    author= 'Rishit kotian',
    author_email= 'rishit.kotian19@gamail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)
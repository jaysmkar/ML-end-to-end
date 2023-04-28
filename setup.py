from setuptools import setup, find_packages 
from typing import List 

# making it as the global variable 
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    """
    Returns: List of requirements to install 
    Input: file_name/path 
    Description: Takes the requirements.txt file as an input and returns the list of requirements to be installed.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements 

# writing the metadata information to the folder.
setup(
    name = 'Machine Learning Modular Code',
    author = 'Jayesh',
    author_email = 'jayeshmandavkar5042@gmail.com',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
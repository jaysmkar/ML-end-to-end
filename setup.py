# importing the dependencies 
from setup import setuptools, find_packages 
from typing import List 

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path:str)->List[str]:
    """
    This function returns a list of requirements for the given files
    Args:
        file_path (str): It is the file path or the name of the file where all the requirements are stored.
    Returns:
        List[str]: It is the list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = requirements.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements 


# Entering the metadata information for the project. 
setup(
    name = 'Machien Learning end to end sales forcasting',
    author = 'Jayesh',
    author_email = 'jayeshmandavkar5042@gmail.com',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
# importing the packags 
from setuptools import setup, find_packages 
from typing import List 

# the global variable
HYPHEN_E_DOT = '-e .'

# This function will return the list of required packages for installation.
def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        # remove the -e . in from the requirements file 
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements 

# entering some metadata information for the project. 
setup(
    name = "Machine Learning sales forcsting model",
    author = 'Jayesh',
    author_email = 'jayeshmandavkar5042@gmail.com',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
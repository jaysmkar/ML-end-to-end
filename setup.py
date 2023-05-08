from setup import setuptools, find_packages
from typing import List 

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str) -> List[str]:
    """ 
    This function will return the list of requirements which will be passed to the install_requires
    which when further used to install requirements file.
    
    args: 
    file_path: It is the path to requirements file or may be the name of requirements file 
    output: It is the list of packages in requirements file 
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = requirements.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

# This is the metadata information about the sales forcasting project
setup(
    name = 'end to end sales forcasting machine learning with deployment',
    author = 'Jayesh',
    author_email = 'jayeshmandavkar5042@gmail.com',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
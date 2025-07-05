from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj if req.strip()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Vivek',
    author_email='patelvivek8874@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

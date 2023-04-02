from setuptools import find_packages,setup
# this find_packages find all the packages avaialble in the directory that we are creating 
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
# in reading the lines there is a problem regarding 


setup(
name="mlproject",
version="0.0.1",
author="melika",
author_email="zabedini164@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requrements.txt")
#["pandas","numpy","seaborn","sklearn","matplotlib"]
)
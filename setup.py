# setup.py (à la racine, par exemple dans C:\Users\buras\Documents\stage\setup.py)
from setuptools import setup, find_packages

setup(
    name="PyAdverseSearch",
    version="0.1",
    packages=find_packages(),  # Ceci trouvera le package PyAdverseSearch et tous ses sous-packages
)

from unicodedata import name
from setuptools import setup

setup(
    name = "paquete",
    version="1.0",
    description="Paquete de ejemplo",
    author="Hernán Quintero",
    author_email="hcquinteroz@gmail.com",
    url="https://hquintero.info",
    scripts=[],
    packages=["paquete", "paquete.adios", "paquete.hola"]
)
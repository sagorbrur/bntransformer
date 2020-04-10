import codecs
import setuptools


setuptools.setup(
    name="bntransformer",
    version="1.0",
    author="Sagor Sarker",
    author_email="sagorhem3532@gmail.com",
    description="bengali transformer bengali language processing state of the art transformer",
    long_description=codecs.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sagorbrur/bntransformer",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=[
        "transformers",
    ],
)

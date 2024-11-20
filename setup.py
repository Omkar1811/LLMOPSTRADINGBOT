from setuptools import setup,find_packages

setup(

    name="financebot",
    version="0.0.1",
    author="Omkar",
    author_email="omkar@gmail.com",
    packages=find_packages(),
    install_requires=[
    "langchain",
    "langchain-openai",
    "langchain-astradb",
    "datasets",
    "pypdf",
    "python-dotenv",
    "flask"
]


)
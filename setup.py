import setuptools

with open("README.md", "r", encoding= "utf-8") as f:
    long_description = f.read()

__version__= "0.0.0"

REPO_NAME = "text-summariser-project-"
AUTHOR_USER_NAME = "nadeeramunasinghe"
SRC_REPO = 'TextSummarizer'
AUTHOR_EMAIL = "ntnadeeram@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    description= "A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir ={"":"src"},
    packages=setuptools.find_packages(where="src") 
)
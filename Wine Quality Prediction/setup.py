import setuptools

with open("README.md","r") as f:
    long_description = f.read()

#__version__ = "0.0.0"

NAME_OF_REPOSITORY = "Wine Quality Prediction"
USER_NAME = "amithvardhan99"
SOURCE_REPO = "misc"
AUTHOR_EMAIL = "amithvardhangd3@gmail.com"
URL = f"https://github.com/{USER_NAME}/{SOURCE_REPO}/"

setuptools.setup(
    name = SOURCE_REPO,
    #version = __version__,
    author = USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "This is the ML project on prediction of wine quality",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = URL,
    project_urls = {
        "BugTracker" : f"{URL}/issues",
    },
    packages = setuptools.find_packages(where="src")
)
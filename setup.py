import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="freezer_escape_room",
    version="0.0.1",
    author="Craig Moore",
    author_email="craigtmoore@gmail.com",
    description="An escape room puzzle",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/craigtmoore/freezer_escape_room",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


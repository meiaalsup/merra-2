import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="merra2",
    version="0.0.1",
    author="Meia Alsup",
    author_email="meia.alsup@gmail.com",
    description="Downloader for data from NASA MERRA2 model and dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meiaalsup/merra2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

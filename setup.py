import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", 'r') as f:
    reqs = f.read().splitlines()

setuptools.setup(
    name="food-recognition",
    version='0.0.1',
    author="Cp Tripathi",
    author_email="tripathi.co07@gmail.com",
    description="A Baseline Food Recognition using Theseus - A general template for most Pytorch projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chandraPrakash-tripathi/food_model",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7',
    install_requires=reqs,
)

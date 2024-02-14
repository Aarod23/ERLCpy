import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ERLC",                 
    version="1.2.2",                     
    author="mark.api",                    
    description="An API wrapper for the ERLC API",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                     
    python_requires='>=3.6',               
    install_requires=[]                  
)
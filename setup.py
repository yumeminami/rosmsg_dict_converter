from setuptools import setup, find_packages

setup(
    name="rosmsg_dict_converter",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
        "rich"
        "pydantic"
    ],
    author="Wing mun Fung",
    author_email="fengrongman@gmail.com",
    description="Provide a  converter to convert ROS message to dict and vice versa",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)

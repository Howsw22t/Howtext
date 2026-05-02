from setuptools import setup, find_packages

setup(
    name="HowText",
    version="0.1.0",
    author="Howsweet_0803", 
    description="Real-time rainbow text engine with emoji-to-unicode conversion",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
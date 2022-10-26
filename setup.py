from distutils.core import setup

setup(
    name="quick",
    version="0.0",
    description="Quick start with python and pytest",
    author="<>",
    author_email="<>@gmail.com",
    install_requires=[
        # ... write packages that are required for the project
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
        ]
    },
    package_dir={"": "src"},
    packages=[],
)

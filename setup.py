from setuptools import setup, find_packages
from recipes_ai import __version__

setup(
    name="recipes_ai",
    version=__version__,
    description="Deep Learning-based recipe generator",
    long_description="Computer Vision, Natural Language Processing and Web scraping for source of data.",
    url="",
    author="Daniela Simancas-Mateus",
    author_email="dan.simancas@gmail.com",
    license="MIT License",
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
    extras_require={
        "docs": [
            "jupyter",
            "jupytext",
            "nbsphinx",
            "nbsphinx-link",
            "recommonmark",
            "sphinx",
            "sphinx_copybutton",
            "sphinx_rtd_theme",
        ],
        "test": ["pytest", "tox"],
        "dev": ["black", "rope", "pylint"],
    },
    package_data={"recipes_ai": ["notebooks/*.ipynb"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)

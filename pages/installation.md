<<<<<<< HEAD
# ViMMS Installation Guide

## 🌟 Stable Release
ViMMS is designed for Python 3 and above. Install the latest stable release with the following command:

```bash
pip install vimms
```
Check out the latest versions on the [Release page](https://github.com/glasgowcompbio/vimms/releases) or [PyPi](https://pypi.org/project/vimms/#history).

**🕰 Older Releases**

For those interested in ViMMS version 1.0 as used in our [original paper](https://www.mdpi.com/2218-1989/9/10/219), you can get it [here](https://zenodo.org/badge/latestdoi/196360601). 
Be aware that it's quite outdated now.
For other previous releases, head over to the [Releases](https://github.com/glasgowcompbio/vimms/releases) page on GitHub. 
This include releases to support other papers.

**🔧 Development Version**

To get the latest features and fixes (still under development), clone the repository:

```$ git clone https://github.com/glasgowcompbio/vimms.git```

You can then set up the environment using [Anaconda Python](https://www.anaconda.com) or [Poetry](https://python-poetry.org).
We recommend using Conda.

There is also support for using [Pipenv](https://pipenv.pypa.io/en/latest/) through the included Pipfile in the repo, but 
going forward that will not be maintained anymore.

***Setting up with Anaconda:***
```
$ cd vimms
$ conda env create --file environment.yml
$ conda activate vimms
$ jupyter lab (to test notebooks)
```

***Setting up with Poetry:***
```
$ cd vimms
$ pip install poetry (if you don't have it)
$ poetry install
$ poetry shell
$ jupyter lab (to test notebooks)
```

***Setting up with Pipenv:***
```
$ cd vimms
$ pip install pipenv (if you don't have it)
$ pipenv install
$ pipenv shell
```

# 🧪 Testing ViMMS

Unit tests are located in the `tests` folder. Use the scripts `run_tests.sh` or `run_tests.bat` to execute them.
=======
# Installation Guide

**Stable Release**

ViMMS is compatible with Python 3 or newer. You can install the latest stable release using pip or pipenv:

```$ pip install vimms```
or
```$ pipenv install vimms```

To verify the current version, visit the [Release page](https://github.com/glasgowcompbio/vimms/releases) or [PyPi](https://pypi.org/project/vimms/#history).

**Older Release**

The ViMMS 1.0 version used in our [original paper](https://www.mdpi.com/2218-1989/9/10/219) can be downloaded [here](https://zenodo.org/badge/latestdoi/196360601). Please note, this version is now significantly out of date.

**Development Version**

For the most recent codebase (still under development), clone this repository:

```$ git clone https://github.com/glasgowcompbio/vimms.git```

The dependencies can be managed using either [Pipenv](https://pipenv.pypa.io/en/latest/) or [Anaconda Python](https://www.anaconda.com).

***With Pipenv:***

1. Install pipenv.
2. Run `$ pipenv install` within the cloned repo to create a new virtual environment and install required packages.
3. Enter the virtual environment using `$ pipenv shell`.

***With Anaconda Python:***

1. Install Anaconda Python.
2. Run `$ conda env create --file environment.yml` within the cloned repo to create a new virtual environment and install required packages.
3. Access the virtual environment by typing `$ conda activate vimms`.

# Test Cases

Unit tests demonstrating simulation execution are in the `tests` folder. Use scripts `run_tests.sh` or `run_tests.bat` to run these tests.
>>>>>>> 84f8a4c4993f6138f7d9b613ad41a8f79e35b62d

Run individual test classes with:

```$ python -m pytest <module>::<class>```

For example:

```$ python -m pytest tests/integration/test_controllers.py::TestSMARTROIController```

Include `-s` switch for test output:

```$ python -m pytest -s tests/integration/test_controllers.py::TestSMARTROIController```
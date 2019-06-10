# ML_DevOPs
![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightblue.svg)

🐍🤖 Tutorial on DevOps for Data Science - this uses Azure pipelines for the DevOps implementation

### 🚀 Detailed set up instructions
The detailed set up instructions including how to create your virtual environment and to get an Azure account can be found at 👉🏼 [https://ml-devops-tutorial.readthedocs.io/en/latest/setup.html](https://ml-devops-tutorial.readthedocs.io/en/latest/setup.html).

---

## Pre requisites

### Python 3.x

We will be using [Python](https://www.python.org/). so we recommend you get the latest version, which is 3.7

### Git 
[Git](https://git-scm.com/) is a version control software that records changes
to a file or set of files. Git is especially helpful for software developers
as it allows changes to be tracked (including who and when) when working on a
project.

To download Git, go to the following link and choose the correct version for your
operating system: <https://git-scm.com/downloads>.

### GitHub

GitHub is a web-based service for version control using Git. You will need
to set up an account at <https://github.com>. Basic GitHub accounts are
free and you can now also have private repositories.

## IDE supporting Python

Text editors are tools with powerful features designed to optimize writing code.
There are several text editors that you can choose from.

Get VS code using 👉🏼 [this link](https://code.visualstudio.com//?wt.mc_id=mlops-github-taallard). This is your facilitator's favourite 💜 and it is worth trying.

If you decide to go for VSCode make sure to also
have the [Python extension](https://marketplace.visualstudio.com/itemdetails?itemName=ms-python.python&wt.mc_id=mlops-github-taallard)
installed. This will make your life so much easier (and it comes with a lot of nifty
features 😎).

## Setup


### Basic setup

1. Clone this repository. From a terminal:
   ```
   git clone https://github.com/trallard/ml_devops_tutorial.git
   ```
2. Change into the setup directory
    ```
    cd setup
    ```
3. Install the requirements:
    ```
    pip install -r requirements
    pip install --upgrade azureml-sdk
    ```

## Additional resources

📖 We will be using Azure Pipelines during the workshop so make sure to visit the docs before following the tutorial using 👉🏼[this link](https://docs.microsoft.com/en-gb/azure//?wt.mc_id=mlops-github-taallard) 🚀🚀

Note that we also use the Python Azure Machine learning SDK 👉🏼 [check the docs here](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/intro?view=azure-ml-py/?wt.mc_id=mlops-github-taallard)


🚀 PRs and Issues are welcome

### License

[![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/80x15.png)](https://creativecommons.org/licenses/by/4.0/)


This repo is licensed using a CC-BY so you are free to use, remix, and share so long attribution is provided to the original author.
# ML_DevOPs
🐍🤖 Tutorial on DevOps for Data Science - this uses Azure pipelines for the DevOps implementation

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

Get VS code using 👉🏼 [this link](https://code.visualstudio.com//?wt.mc_id=mldevops-github-taallard). This is your facilitator's favourite 💜 and it is worth trying.

If you decide to go for VSCode make sure to also
have the [Python extension](https://marketplace.visualstudio.com/itemdetails?itemName=ms-python.python&wt.mc_id=mldevops-github-taallard)
installed. This will make your life so much easier (and it comes with a lot of nifty
features 😎).

## Setup

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
    pip install azureml-sdk
    ```
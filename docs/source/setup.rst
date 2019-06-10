Setup
===============
This section will guide you through the pre requisites for the workshop.
Please make sure to install the libraries before the workshop as the conference WiFi 
can get quite slow when having too many people downloading and installing things at the same 
time.

Make sure to follow all the steps as detailed here especially :ref:`attendees`
as there are specific details for the PyCon setup that needs to be done in advance. 

Python 3.x
++++++++++

3.7 Preferred

We will be using `Python <https://www.python.org/>`_.
Installing all of Python's packages individually can be a bit
difficult, so we recommend using `Anaconda <https://www.anaconda.com/>`_ which
provides a variety of useful packages/tools.

To download Anaconda, follow the link https://www.anaconda.com/download/ and select
Python 3. Following the download, run the installer as per usual on your machine.

If you prefer not using Anaconda then this `tutorial <https://realpython.com/installing-python/>`_ can help you with the installation and 
setup.

If you already have Python installed but not via Anaconda do not worry.
Make sure to have either ``venv`` or ``pipenv`` installed. Then follow the instructions to set 
your virtual environment further down.

Git
+++

`Git <https://git-scm.com/>`_ is a version control software that records changes
to a file or set of files. Git is especially helpful for software developers
as it allows changes to be tracked (including who and when) when working on a
project.

To download Git, go to the following link and choose the correct version for your
operating system: https://git-scm.com/downloads.

Windows
--------

Download the  `git for Windows installer <https://gitforwindows.org/>`_ . 
Make sure to select "use Git from the Windows command prompt" 
this will ensure that Git is permanently added to your PATH. 

Also select "Checkout Windows-style, commit Unix-style line endings" selected and click on "Next".

This will provide you both git and git bash. We will use the command line quite a lot during the workshop 
so using git bash is a good option.

GitHub
++++++

GitHub is a web-based service for version control using Git. You will need
to set up an account at `https://github.com <https://github.com>`_. Basic GitHub accounts are
free and you can now also have private repositories.

Text Editors/IDEs
+++++++++++++++++++

Text editors are tools with powerful features designed to optimize writing code.
There are several text editors that you can choose from.
Here are some we recommend:

- `VS code <https://code.visualstudio.com//?wt.mc_id=PyCon-github-taallard>`_: this is your facilitator's favourite 💜 and it is worth trying if you have not checked it yet
- `Pycharm <https://www.jetbrains.com/pycharm/download/>`_
- `Atom <https://atom.io>`_

We suggest trying several editors before settling on one.

If you decide to go for VSCode make sure to also
have the `Python extension <https://marketplace.visualstudio.com/itemdetails?itemName=ms-python.python&wt.mc_id=PyCon-github-taallard>`_
installed. This will make your life so much easier (and it comes with a lot of nifty
features 😎).


Microsoft Azure
+++++

You will need to get an Azure account as we will be using this to deploy the 
Airflow instance.

.. note:: If you are doing this tutorial in person then your
    facilitator will provide you with specific instructions to set up your Azure subscription. If you have not received these please let your facilitator know ASAP.

Follow `this link <https://azure.microsoft.com/en-us/free//?wt.mc_id=mlops-github-taallard>`_ 
to get an Azure free subscription. This will give you 150 dollars in credit so you
can get started getting things up and follow the materials.


Creating a virtual environment
+++++++++++++++++++++++++++++++

You will need to create a virtual environment to make sure that you have the right packages and setup needed to follow along the tutorial.
Follow the instructions that best suit your installation.

Anaconda
--------

If you are using Anaconda first you will need to make a directory for the tutorial, for example ``mkdir airflow-tutorial``.
Once created make sure to change into it using ``cd airflow-tutorial``.

Next, make a copy of this `environment.yaml <https://raw.githubusercontent.com/trallard/airflow-tutorial/master/environment.yaml>`_
 and install the 
dependencies via ``conda env create -f environment.yml``.
Once all the dependencies are installed you can activate your environment through the following commands 
::
    source activate airflow-env # Mac
    activate airflow-env        # Windows and Linux
To exit the environment you can use 
::
    deactivate airflow-env    


pipenv
-------

Create a directory for the tutorial, for example:
::
    mkdir airflow-tutorial 

and change your working directory to this newly created one ``cd airflow-tutorial``.

Once then make a copy of this `Pipfile <https://raw.githubusercontent.com/trallard/airflow-tutorial/master/Pipfile>`_ 
in your new directory and install via ``pipenv install``.
This will install the dependencies you need. This might take a while so you can make yourself a brew in the meantime.

Once all the dependencies are installed you can run ``pipenv shell`` which will start a session with the correct virtual environment activated. To exit the shell session using ``exit``.

virtualenv
-----------
Create a directory for the tutorial, for example :
::
    mkdir airflow-tutorial 
and change directories into it (``cd airflow-tutorial``).
Now you  need to run venv 
::
    python3 -m venv env/airflow # Mac and Linux 
    python -m venv env/airflow  # Windows

this will create a virtual Python environment in the ``env/airflow`` folder.
Before installing the required packages you need to activate your virtual environment: 
::
    source env/bin/activate # Mac and Linux 
    .\env\Scripts\activate  # Windows 

Make a copy of `this requirements file <https://raw.githubusercontent.com/trallard/airflow-tutorial/master/requirements.txt>`_ 
in your new directory.
Now you can install the packages using via pip ``pip install -r requirements.txt``

To leave the virtual environment run ``deactivate``


.. _attendees:

🐍 In person workshop attendees  
----------------------------------    

Azure Pass account
~~~~~~~~~~~~~~~~~~~~
As an in person workshop attendee, you will be issued with an Azure pass worth 200 dollars with a 90 days validity.
You will not need to add credit card details to activate but you will need to follow this process to redeem your credits.

1. Send an email your facilitator at trallard@bitsandchips.me with the subject line ``PyConCZ - Azure pass``, they will send you an email with a `unique` code to redeem. Please do not share with anyone, 
this is a single-use pass and once activated it will be invalid.

2. Make sure to visit 👉🏼 `this website <https://docs.microsoft.com/en-us/azure//?wt.mc_id=mlops-github-taallard>`_ before anything else. 

3. Go to `this site <https://www.microsoftazurepass.com/?wt.mc_id=mlops-github-taallard>`_ to redeem your pass. 
We recommend doing this in a private/incognito window. You can then click start and attach your new pass to your existing account. 

If you see the following error (see image)

.. image:: _static/mssignin.png

you can go to `this site <https://signup.live.com//?wt.mc_id=mlops-github-taallard>`_  to register the email and proceed.

4. Confirm your email address. You will then be asked to add the promo code that you were sent by your instructor.
Do not close or refresh the window until you have received a confirmation that this has been successful. 

.. image:: _static/4.jpg

5. Activate your subscription: click on the activate button and fill in the personal details

Again once completed, do not refresh the window until you see this image

.. image:: _static/12.png

At this point, your subscription will be ready, click on Get started to go to your Azure portal

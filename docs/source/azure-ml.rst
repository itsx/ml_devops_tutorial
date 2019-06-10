Getting started with Azure Machine Learning
=============================================

Azure Machine Learning service provides a cloud-based environment you can use to 
prep data, train, test, deploy, manage, and track machine learning models. 
Start training on your local machine and then scale out to the cloud. 
The service fully supports open-source technologies such as PyTorch, TensorFlow, 
and scikit-learn and can be used for any kind of machine learning, from classical ml to deep learning, supervised and unsupervised learning.

Explore and prepare data, train and test models, and deploy them using rich tools such as:

- A visual interface
- Jupyter notebooks
- Visual Studio Code Extension

Before you start training and deploying machine learning models using VS Code, 
you need to create an :ref:`MLWorkspace`.

1. Click the Azure icon in the Visual Studio Code activity bar. The Azure Machine Learning sidebar appears.

   [![install](./media/CreateaWorkspace.gif)](./media/CreateaWorkspace.gif#lightbox)


1. Right-click your Azure subscription and select **Create Workspace**. A list appears. In the animated image, the subscription name is 'Free Trial' and the workspace is 'TeamWorkspace'.

1. Select an existing resource group from the list or create a new one using the wizard in the Command Palette.

1. In the field, type a unique and clear name for your new workspace. In the screenshots, the workspace is named 'TeamWorkspace'.

1. Hit enter and the new workspace is created. It appears in the tree below the subscription name.

1. Right-click on the Experiment node and choose **Create Experiment** from the context menu.  Experiments keep track of your runs using Azure Machine Learning.

1. In the field, enter a name your experiment. In the screenshots, the experiment is named 'MNIST'.

1. Hit enter and the new experiment is created. It appears in the tree below the workspace name.

1. You can right-click on an Experiment in a Workspace and select 'Set as Active Experiment'. The **'Active'** experiment is the experiment you are currently using and your open folder in VS Code will be linked to this experiment in the cloud. This folder should contain your local Python scripts.

   Now each of your runs will be associated with the active experiment, so all of your key metrics will be stored in the experiment history and the models you train will get automatically uploaded to Azure Machine Learning and stored with your experiment metrics and logs.

   [![Attach a folder in VS Code](./media/CreateAnExperiment.gif)](./media/CreateAnExperiment.gif#lightbox)

## Next steps
- To learn how to create and manage compute resources in Azure Machine Learning from within VS Code, see [Create and manage compute targets in Visual Studio Code](manage-compute-aml-vscode.md)
- To learn how to train models and manage your experiments from Visual Studio Code, see [Training models and managing experiments in Visual Studio Code](train-models-aml-vscode.md)
- To learn how to deploy and manage models from Visual Studio Code, see [Deploying and managing models in Visual Studio Code](deploy-models-aml-vscode.md)

Glossary
=========

.. _MLWorkspace:

Azure ML workspace
""""""""""""""""""""

The workspace is the top-level resource for Azure Machine 
Learning service, providing a centralized place to work with all the artifacts you create when you use Azure Machine Learning service. The workspace keeps a history of all training runs, including logs, metrics, output, and a snapshot of your scripts. 
You use this information to determine which training run produces the best model.

🔎 Learn more `here <https://docs.microsoft.com/azure/machine-learning/service/concept-workspace?WT.mc_id=mlops-github-taallard>`_.

.. _ServicePrincipal:

Service principal
"""""""""""""""""""
To access resources that are secured by an Azure AD tenant, the entity that requires access must be represented by a security principal. This is true for both users (user principal) and applications (service principal).

The security principal defines the access policy and permissions for the user/application in the Azure AD (Azure Aztive Directory) tenant. 
This enables core features such as authentication of the user/application during sign-in, and authorization during resource access.

🔎 Learn more `here <https://docs.microsoft.com/azure/active-directory/develop/app-objects-and-service-principals?WT.mc_id=mlops-github-taallard>`_.

.. _RBAC:

RBAC:
"""""""
Role Based Access Control (RBAC) is how you manage access to Azure resources. Basically it is how permissions are assigned to 
a specific resource.

They consist of a security principal, role definition, and scope.

.. image:: https://docs.microsoft.com/en-us/azure/role-based-access-control/media/overview/rbac-overview.png


🔎 Learn more `here <https://docs.microsoft.com/azure/role-based-access-control/overview?WT.mc_id=mlops-github-taallard>`_.


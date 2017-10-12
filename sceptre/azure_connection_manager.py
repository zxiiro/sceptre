# -*- coding: utf-8 -*-

"""
sceptre.azure_connection_manager

This module implements an AzureConnectionManager class, which manages
AzureRM API calls.
"""


import os.path
import json
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import DeploymentMode


class AzureConnectionManager(object):
    """ Initialize the ACM class with subscription & resource group.

    :raises KeyError: If AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_TENANT_ID
        variables or not defined
    """
    def __init__(self, subscription_id, deployment_name, location,
                 resource_group):
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.deployment_name = deployment_name
        self.location = location

        self.credentials = ServicePrincipalCredentials(
            client_id=os.environ['AZURE_CLIENT_ID'],
            secret=os.environ['AZURE_CLIENT_SECRET'],
            tenant=os.environ['AZURE_TENANT_ID']
        )
        self.client = ResourceManagementClient(self.credentials,
                                               self.subscription_id)

    def deploy(self):
        """Deploy the template to a resource group."""
        self.client.resource_groups.create_or_update(
            self.resource_group,
            {
                'location': self.location
            }
        )

        template_path = os.path.join(os.path.dirname(__file__),
                                     'templates',
                                     'azure-ubuntu-vm-template.json')
        with open(template_path, 'r') as template_file_fd:
            template = json.load(template_file_fd)

        parameters = {}

        parameters = {k: {'value': v} for k, v in parameters.items()}

        deployment_properties = {
            'mode': DeploymentMode.incremental,
            'template': template,
            'parameters': parameters
        }

        deployment_async_operation = self.client.deployments.create_or_update(
            self.resource_group,
            self.deployment_name,
            deployment_properties
        )
        deployment_async_operation.wait()

    def destroy(self):
        """Destroy the given resource group"""
        self.client.resource_groups.delete(self.resource_group)

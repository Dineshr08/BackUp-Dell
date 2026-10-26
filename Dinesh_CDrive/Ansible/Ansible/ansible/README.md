# CFGAAS

This project involves the configuration as a service (CFGaaS) environment using Ansible.

Configuring roles and playbooks that are part of AMaaS (Artifactory as a service) project. 

## Inventories
Remote hosts or grouping of host can be setup at Inventories folder. (This can be sourced to AWX tower for deployment)

## Roles
Roles provide a framework for fully independent, or interdependent collections of variables, tasks, files, templates, and modules.
These are small functionality which can be independently used but have to be used within playbooks. All roles in the project needs to be unders roles/** folder

## Playbooks
Each playbook is an aggregation of one or more plays in it. The function of a play is to map a set of instructions defined against a particular host. All playbook in our project needs to be created under playbooks/** folder

## Role Variables
Defined in roles/../vars. These variables can be set in vars folder or externally using playbook. 
A general good practice is to define them in vars folder

## Dependencies
None.
testing push
## How it works

Example of how to use this role:

    - hosts: servers
      roles:
         - { role: artifactory }
         
    - hosts: your-servers
      roles:
        - { role: java, java_packages: java-11-openjdk}

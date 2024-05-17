#!/bin/bash

# Run Terraform to provision infrastructure
terraform init
terraform apply -auto-approve

# Get the public IP of the instance
PUBLIC_IP=$(terraform output -raw public_ip)

# Run Ansible to configure the instance
ansible-playbook -i "${PUBLIC_IP}," --private-key ~/path/to/private/key ansible/setup.yml

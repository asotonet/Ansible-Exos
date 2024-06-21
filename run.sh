#!/bin/bash

# Ejecutar los scripts .py
python3 convertcsv.py
python3 add_fingerprint.py

# Ejecutar el playbook de Ansible
ansible-playbook -i hosts.ini playbook.yml 
python3 remove_knowhosts.py

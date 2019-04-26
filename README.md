ansible-role-packages
=========

Ansible role to install packages required by roles

Using this role
--------------

The role needs to be loaded dynamically during the plays and the dictionary of parameters to pass to the role.

Role Variables
--------------

This role will need to be provided with a dictionary of variables that have this structure.

```
namespace_packages: # Namespace variable of the role
  redhat: # Lower case version of os_family 
    - package
      # Package to be installed, include version if 
      # required 
    update_all: (true:false) # Perform full package update
  debian:
    - package
    update_cache: (yes|no) # Force the update of the apt-cache 
    update_all: (true:false)
```

Example Playbook
----------------

Example import:
```
...
- import_role:
    name: ansible-role-packages
  vars:
    packages: "{{ namespace_packages }}"
...
```
Example Vars:

```
test_packages:
  redhat:
    - '{{ yum packages }}
  debian:
    - {{ debian packages }}
    update_cache: yes
```
License
-------

MIT

Author Information
------------------
The Development Range Engineering, Architecture, and Modernization (DREAM) Team

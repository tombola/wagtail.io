# Wagtail.io

This is the source code to [Wagtail's website](https://wagtail.io)

## Installation

You firstly need to install [git](https://git-scm.com), [Vagrant](https://www.vagrantup.com/) and [Virtualbox](https://www.virtualbox.org/). Once they are installed, run the following commands to get up and running:

```
git clone https://github.com/wagtail/wagtail.io.git
cd wagtail.io
vagrant up
```

This will download the base image and provision a local VM that will run the site locally.

## Usage

Common Vagrant commands:

 - ``vagrant up`` starts the VM
 - ``vagrant halt`` stops the VM
 - ``vagrant ssh`` opens a shell in the VM
 - ``vagrant destroy`` deletes the VM

Shortcut commands:

Within the VM shell, you can run ``./manage.py`` to run any Django management command. But we have added a couple of shortcuts to save on typing:

 - ``dj <command> [args]`` - Runs a management command (eg, ``dj shell``)
 - ``djrun`` - Starts the webserver on port 8000

---
hide:
  - navigation
  - toc
---

## Requirements

- Python 3.10: ADT requires Python 3.10 or later. Make sure you have Python 3.10 installed on your system before proceeding.

## Installation

`pip install ansible-dev-tools`

Once installation is completed, see the [Getting Started](getting-started.md) guide for more details about ADT usage.

### Latest Releases

- GitHub
  To view the latest releases, see the [ADT GitHub releases page](https://github.com/ansible/ansible-dev-tools/releases). Each release includes detailed release notes outlining new features, improvements, and bug fixes.

- PyPI
  The [PyPI page for ADT](https://pypi.org/project/ansible-dev-tools/) provides information on the latest stable release and allows you to download specific versions of the package.

## Upgrade

To upgrade ADT to the latest version, use the following pip command:

`pip install --upgrade ansible-dev-tools`

## Downgrade

If needed, you can downgrade ADT to a specific version using the following pip command:

`pip install ansible-dev-tools==desired-version`

## Uninstallation

If you need to uninstall ADT, use the following pip command:

`pip uninstall ansible-dev-tools`

## Usage

In addition to installing each of the above tools, `ansible-dev-tools` provides an easy way to show the versions of the content creation tools that make up the current development environment.

```
$ adt --version
ansible-builder                          3.0.0
ansible-core                             2.16.0
ansible-creator                          1.0.0
ansible-dev-tools                        1.0.0
ansible-lint                             6.22.0
ansible-navigator                        3.5.0
ansible-sign                             0.1.1
molecule                                 6.0.2
pytest-ansible                           4.1.1
tox-ansible                              2.0.14
```

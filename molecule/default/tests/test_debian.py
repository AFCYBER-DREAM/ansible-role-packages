import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('package-debian')


def test_debian_package(host):
    package = host.package('gcc')

    assert package.is_installed

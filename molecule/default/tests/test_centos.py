import os
import datetime

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('centos')


def test_installed_packages(host):
    gcc = host.package('gcc')

    assert gcc.is_installed


def test_cache_update(host):
    cache = host.file('/var/cache/yum/x86_64/7/updates/cachecookie')
    time_delta = datetime.datetime.now() - datetime.timedelta(minutes=10)

    assert cache.mtime > time_delta

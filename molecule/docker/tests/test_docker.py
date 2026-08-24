import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_mariadb_service_file_exists(host):
    assert host.file("/etc/systemd/system/mariadb.service").exists


def test_mariadb_default_config_exists(host):
    assert host.file("/etc/default/mariadb").exists


def test_mariadb_service_enabled(host):
    service = host.service("mariadb")
    assert service.is_enabled


def test_mariadb_service_running(host):
    service = host.service("mariadb")
    assert service.is_running


def test_mariadb_listening_on_3306(host):
    assert host.socket("tcp://127.0.0.1:3306").is_listening

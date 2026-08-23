import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_mariadb_apt_source_removed(host):
    assert not host.file("/etc/apt/sources.list.d/mariadb.list").exists


def test_mariadb_keyring_removed(host):
    assert not host.file("/etc/apt/keyrings/mariadb-keyring.gpg").exists


def test_mariadb_server_package_installed(host):
    assert host.package("mariadb-server").is_installed


def test_mariadb_service_enabled(host):
    service = host.service("mariadb")
    assert service.is_enabled


def test_mariadb_service_running(host):
    service = host.service("mariadb")
    assert service.is_running


def test_mariadb_unix_socket_exists(host):
    assert host.socket("unix:///run/mysqld/mysqld.sock").is_listening

import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_service_file(host):
    file = host.file("/etc/systemd/system/mariadb.service")
    assert file.exists


def test_running_and_enabled(host):
    svc = host.service("mariadb")
    assert svc.is_running
    assert svc.is_enabled


def test_server_socket(host):
    assert host.socket("tcp://127.0.0.1:3306").is_listening

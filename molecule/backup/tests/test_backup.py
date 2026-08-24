import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_mariadb_backup_script_exists(host):
    assert host.file("/usr/local/bin/mariadb-backup").exists


def test_mariadb_backup_script_executable(host):
    assert host.file("/usr/local/bin/mariadb-backup").mode == 0o770


def test_mariadb_backup_service_exists(host):
    assert host.file("/etc/systemd/system/mariadb-backup.service").exists


def test_mariadb_backup_timer_exists(host):
    assert host.file("/etc/systemd/system/mariadb-backup.timer").exists


def test_mariadb_backup_timer_enabled(host):
    timer = host.service("mariadb-backup.timer")
    assert timer.is_enabled

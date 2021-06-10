# work

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/mariadb) [![Testing Build](https://github.com/rolehippie/mariadb/workflows/testing/badge.svg)](https://github.com/rolehippie/mariadb/actions?query=workflow%3Atesting) [![Readme Build](https://github.com/rolehippie/mariadb/workflows/readme/badge.svg)](https://github.com/rolehippie/mariadb/actions?query=workflow%3Areadme) [![Galaxy Build](https://github.com/rolehippie/mariadb/workflows/galaxy/badge.svg)](https://github.com/rolehippie/mariadb/actions?query=workflow%3Agalaxy) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/mariadb)](https://github.com/rolehippie/mariadb/blob/master/LICENSE) 

Ansible role to install and configure a simple MariaDB. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

## Table of content

* [Default Variables](#default-variables)
  * [mariadb_backup_addition_script](#mariadb_backup_addition_script)
  * [mariadb_backup_cron](#mariadb_backup_cron)
  * [mariadb_backup_enabled](#mariadb_backup_enabled)
  * [mariadb_backup_formatting](#mariadb_backup_formatting)
  * [mariadb_backup_ignore](#mariadb_backup_ignore)
  * [mariadb_backup_path](#mariadb_backup_path)
  * [mariadb_backup_retention](#mariadb_backup_retention)
  * [mariadb_bind_address](#mariadb_bind_address)
  * [mariadb_exporter_args](#mariadb_exporter_args)
  * [mariadb_exporter_collect_info_schema_tables](#mariadb_exporter_collect_info_schema_tables)
  * [mariadb_exporter_download](#mariadb_exporter_download)
  * [mariadb_exporter_enabled](#mariadb_exporter_enabled)
  * [mariadb_exporter_version](#mariadb_exporter_version)
  * [mariadb_extra_databases](#mariadb_extra_databases)
  * [mariadb_extra_users](#mariadb_extra_users)
  * [mariadb_global_databases](#mariadb_global_databases)
  * [mariadb_global_users](#mariadb_global_users)
  * [mariadb_ignore_db_dirs](#mariadb_ignore_db_dirs)
  * [mariadb_limit_number_files](#mariadb_limit_number_files)
  * [mariadb_lower_case_table_names](#mariadb_lower_case_table_names)
  * [mariadb_max_allowed_packet](#mariadb_max_allowed_packet)
  * [mariadb_max_connections](#mariadb_max_connections)
  * [mariadb_packages](#mariadb_packages)
  * [mariadb_root_hosts](#mariadb_root_hosts)
  * [mariadb_root_password](#mariadb_root_password)
  * [mariadb_root_username](#mariadb_root_username)
  * [mariadb_temp_directory](#mariadb_temp_directory)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### mariadb_backup_addition_script

Additional commands at the end of the script

#### Default value

```YAML
mariadb_backup_addition_script:
```

### mariadb_backup_cron

A simple cron timing definition like hourly, daily or weekly

#### Default value

```YAML
mariadb_backup_cron: daily
```

### mariadb_backup_enabled

Enable or disable the backup script

#### Default value

```YAML
mariadb_backup_enabled: false
```

### mariadb_backup_formatting

Date format for the backup folder name

#### Default value

```YAML
mariadb_backup_formatting: '%F'
```

### mariadb_backup_ignore

Ignoring this filter via grep on database selection

#### Default value

```YAML
mariadb_backup_ignore: (_backup|mysql|information_schema|performance_schema)
```

### mariadb_backup_path

Path to store the backups

#### Default value

```YAML
mariadb_backup_path: /var/lib/mysql/_backup
```

### mariadb_backup_retention

Retention period to keep backups

#### Default value

```YAML
mariadb_backup_retention: 7
```

### mariadb_bind_address

Bind address for the server

#### Default value

```YAML
mariadb_bind_address: 0.0.0.0
```

### mariadb_exporter_args

List of arguments joined for the executable

#### Default value

```YAML
mariadb_exporter_args: []
```

### mariadb_exporter_collect_info_schema_tables

Enable info schema tables collector

#### Default value

```YAML
mariadb_exporter_collect_info_schema_tables: true
```

### mariadb_exporter_download

URL to the archive of the release to install

#### Default value

```YAML
mariadb_exporter_download: https://github.com/prometheus/mysqld_exporter/releases/download/v{{
  mariadb_exporter_version }}/mysqld_exporter-{{ mariadb_exporter_version }}.linux-amd64.tar.gz
```

### mariadb_exporter_enabled

Enable the mariadb exporter

#### Default value

```YAML
mariadb_exporter_enabled: true
```

### mariadb_exporter_version

Version of the release to install

#### Default value

```YAML
mariadb_exporter_version: 0.12.1
```

### mariadb_extra_databases

List of additional databases to create

#### Default value

```YAML
mariadb_extra_databases: []
```

#### Example usage

```YAML
mariadb_extra_databases:
  - name: example
    collation: utf8mb4_general_ci
    encoding: utf8mb4
    state: present
  - name: foobar
    state: absent
```

### mariadb_extra_users

List of additional users to create

#### Default value

```YAML
mariadb_extra_users: []
```

#### Example usage

```YAML
mariadb_extra_users:
  - name: example
    password: p433w0rd
    host: '%'
    priv: '*.*:ALL'
    state: present
  - name: foobar
    state: absent
```

### mariadb_global_databases

List of databases to create

#### Default value

```YAML
mariadb_global_databases: []
```

#### Example usage

```YAML
mariadb_global_databases:
  - name: example
    collation: utf8mb4_general_ci
    encoding: utf8mb4
    state: present
  - name: foobar
    state: absent
```

### mariadb_global_users

List of users to create

#### Default value

```YAML
mariadb_global_users: []
```

#### Example usage

```YAML
mariadb_global_users:
  - name: example
    password: p433w0rd
    host: '%'
    priv: '*.*:ALL'
    state: present
  - name: foobar
    state: absent
```

### mariadb_ignore_db_dirs

List of ignored database directories

#### Default value

```YAML
mariadb_ignore_db_dirs: []
```

### mariadb_limit_number_files

Number of allowed open files for systemd service

#### Default value

```YAML
mariadb_limit_number_files: 32768
```

### mariadb_lower_case_table_names

Lowercase table names

#### Default value

```YAML
mariadb_lower_case_table_names: 0
```

### mariadb_max_allowed_packet

Max allowed packet

#### Default value

```YAML
mariadb_max_allowed_packet: 64M
```

### mariadb_max_connections

Max allowed connections

#### Default value

```YAML
mariadb_max_connections: 1000
```

### mariadb_packages

List of packages to install

#### Default value

```YAML
mariadb_packages:
  - mariadb-server
  - mariadb-client
  - mariadb-backup
  - mycli
  - python3-pymysql
```

### mariadb_root_hosts

Allowed hosts for root user

#### Default value

```YAML
mariadb_root_hosts:
  - localhost
```

### mariadb_root_password

Password for the root user

#### Default value

```YAML
mariadb_root_password: root
```

### mariadb_root_username

Username for the root user

#### Default value

```YAML
mariadb_root_username: root
```

### mariadb_temp_directory

Temporary directory used by MariaDB

#### Default value

```YAML
mariadb_temp_directory:
```

## Dependencies

* [rolehippie.docker](https://github.com/rolehippie/docker)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)

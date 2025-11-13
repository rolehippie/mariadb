# mariadb

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/mariadb)
[![General Workflow](https://github.com/rolehippie/mariadb/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/mariadb/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/mariadb/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/mariadb/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/mariadb/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/mariadb/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/mariadb)](https://github.com/rolehippie/mariadb/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.mariadb-blue)](https://galaxy.ansible.com/rolehippie/mariadb)

Ansible role to install and configure a simple MariaDB.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [mariadb_backup_addition_script](#mariadb_backup_addition_script)
  - [mariadb_backup_cron](#mariadb_backup_cron)
  - [mariadb_backup_enabled](#mariadb_backup_enabled)
  - [mariadb_backup_formatting](#mariadb_backup_formatting)
  - [mariadb_backup_ignore](#mariadb_backup_ignore)
  - [mariadb_backup_path](#mariadb_backup_path)
  - [mariadb_backup_retention](#mariadb_backup_retention)
  - [mariadb_bind_address](#mariadb_bind_address)
  - [mariadb_cpu_shares](#mariadb_cpu_shares)
  - [mariadb_database](#mariadb_database)
  - [mariadb_default_folders](#mariadb_default_folders)
  - [mariadb_default_labels](#mariadb_default_labels)
  - [mariadb_default_publish](#mariadb_default_publish)
  - [mariadb_default_volumes](#mariadb_default_volumes)
  - [mariadb_exporter_args](#mariadb_exporter_args)
  - [mariadb_exporter_collect_info_schema_tables](#mariadb_exporter_collect_info_schema_tables)
  - [mariadb_exporter_cpu_shares](#mariadb_exporter_cpu_shares)
  - [mariadb_exporter_default_labels](#mariadb_exporter_default_labels)
  - [mariadb_exporter_default_publish](#mariadb_exporter_default_publish)
  - [mariadb_exporter_download](#mariadb_exporter_download)
  - [mariadb_exporter_enabled](#mariadb_exporter_enabled)
  - [mariadb_exporter_extra_labels](#mariadb_exporter_extra_labels)
  - [mariadb_exporter_extra_publish](#mariadb_exporter_extra_publish)
  - [mariadb_exporter_image](#mariadb_exporter_image)
  - [mariadb_exporter_memory_limit](#mariadb_exporter_memory_limit)
  - [mariadb_exporter_memory_soft_limit](#mariadb_exporter_memory_soft_limit)
  - [mariadb_exporter_memory_swap](#mariadb_exporter_memory_swap)
  - [mariadb_exporter_network](#mariadb_exporter_network)
  - [mariadb_exporter_number_of_cpus](#mariadb_exporter_number_of_cpus)
  - [mariadb_exporter_pull_image](#mariadb_exporter_pull_image)
  - [mariadb_exporter_version](#mariadb_exporter_version)
  - [mariadb_extra_configs](#mariadb_extra_configs)
  - [mariadb_extra_databases](#mariadb_extra_databases)
  - [mariadb_extra_folders](#mariadb_extra_folders)
  - [mariadb_extra_labels](#mariadb_extra_labels)
  - [mariadb_extra_publish](#mariadb_extra_publish)
  - [mariadb_extra_users](#mariadb_extra_users)
  - [mariadb_extra_volumes](#mariadb_extra_volumes)
  - [mariadb_galera_address](#mariadb_galera_address)
  - [mariadb_galera_cluster](#mariadb_galera_cluster)
  - [mariadb_galera_enabled](#mariadb_galera_enabled)
  - [mariadb_galera_name](#mariadb_galera_name)
  - [mariadb_galera_nodes](#mariadb_galera_nodes)
  - [mariadb_galera_primary](#mariadb_galera_primary)
  - [mariadb_global_databases](#mariadb_global_databases)
  - [mariadb_global_users](#mariadb_global_users)
  - [mariadb_ignore_db_dirs](#mariadb_ignore_db_dirs)
  - [mariadb_image](#mariadb_image)
  - [mariadb_innodb_buffer_pool_instances](#mariadb_innodb_buffer_pool_instances)
  - [mariadb_innodb_buffer_pool_size](#mariadb_innodb_buffer_pool_size)
  - [mariadb_innodb_file_per_table](#mariadb_innodb_file_per_table)
  - [mariadb_innodb_flush_log_at_trx_commit](#mariadb_innodb_flush_log_at_trx_commit)
  - [mariadb_innodb_io_capacity](#mariadb_innodb_io_capacity)
  - [mariadb_innodb_max_dirty_pages_pct](#mariadb_innodb_max_dirty_pages_pct)
  - [mariadb_installation](#mariadb_installation)
  - [mariadb_key_buffer_size](#mariadb_key_buffer_size)
  - [mariadb_keyring](#mariadb_keyring)
  - [mariadb_limit_number_files](#mariadb_limit_number_files)
  - [mariadb_lower_case_table_names](#mariadb_lower_case_table_names)
  - [mariadb_max_allowed_packet](#mariadb_max_allowed_packet)
  - [mariadb_max_connections](#mariadb_max_connections)
  - [mariadb_memory_limit](#mariadb_memory_limit)
  - [mariadb_memory_soft_limit](#mariadb_memory_soft_limit)
  - [mariadb_memory_swap](#mariadb_memory_swap)
  - [mariadb_network](#mariadb_network)
  - [mariadb_number_of_cpus](#mariadb_number_of_cpus)
  - [mariadb_oom_score_adjust](#mariadb_oom_score_adjust)
  - [mariadb_packages](#mariadb_packages)
  - [mariadb_password](#mariadb_password)
  - [mariadb_pull_image](#mariadb_pull_image)
  - [mariadb_query_cache_size](#mariadb_query_cache_size)
  - [mariadb_query_cache_type](#mariadb_query_cache_type)
  - [mariadb_root_hosts](#mariadb_root_hosts)
  - [mariadb_root_password](#mariadb_root_password)
  - [mariadb_root_username](#mariadb_root_username)
  - [mariadb_skip_name_resolve](#mariadb_skip_name_resolve)
  - [mariadb_symbolic_links](#mariadb_symbolic_links)
  - [mariadb_temp_directory](#mariadb_temp_directory)
  - [mariadb_timeout_start_sec](#mariadb_timeout_start_sec)
  - [mariadb_upstream_arch](#mariadb_upstream_arch)
  - [mariadb_upstream_mirror](#mariadb_upstream_mirror)
  - [mariadb_upstream_repo](#mariadb_upstream_repo)
  - [mariadb_upstream_version](#mariadb_upstream_version)
  - [mariadb_username](#mariadb_username)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`

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
mariadb_backup_ignore: (_backup|mysql|sys|information_schema|performance_schema)
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

### mariadb_cpu_shares

CPU shares with Docker deployment

#### Default value

```YAML
mariadb_cpu_shares:
```

#### Example usage

```YAML
mariadb_cpu_shares: '512'
```

### mariadb_database

Database used within docker deployment

#### Default value

```YAML
mariadb_database:
```

### mariadb_default_folders

List of default folders to create

#### Default value

```YAML
mariadb_default_folders:
  - /etc/systemd/system/mariadb.service.d
  - /etc/mysql
  - /etc/mysql/mariadb.conf.d
```

### mariadb_default_labels

List of default labels to assign to docker

#### Default value

```YAML
mariadb_default_labels: []
```

### mariadb_default_publish

List of default port publishing for docker

#### Default value

```YAML
mariadb_default_publish: []
```

#### Example usage

```YAML
mariadb_default_publish:
  - 127.0.0.1:3306:3306
```

### mariadb_default_volumes

List of default volumes to mount for docker

#### Default value

```YAML
mariadb_default_volumes:
  - /var/lib/mysql:/var/lib/mysql
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

### mariadb_exporter_cpu_shares

CPU shares with Docker deployment

#### Default value

```YAML
mariadb_exporter_cpu_shares:
```

#### Example usage

```YAML
mariadb_exporter_cpu_shares: '512'
```

### mariadb_exporter_default_labels

List of default labels to assign to docker on OAuth2 Proxy

#### Default value

```YAML
mariadb_exporter_default_labels: []
```

### mariadb_exporter_default_publish

List of default port publishing for docker on OAuth2 Proxy

#### Default value

```YAML
mariadb_exporter_default_publish: []
```

#### Example usage

```YAML
mariadb_exporter_default_publish:
  - 127.0.0.1:9104:9104
```

### mariadb_exporter_download

URL to the archive of the release to install

#### Default value

```YAML
mariadb_exporter_download: 
  https://github.com/prometheus/mysqld_exporter/releases/download/v{{ 
  mariadb_exporter_version }}/mysqld_exporter-{{ mariadb_exporter_version 
  }}.linux-amd64.tar.gz
```

### mariadb_exporter_enabled

Enable the mariadb exporter

#### Default value

```YAML
mariadb_exporter_enabled: true
```

### mariadb_exporter_extra_labels

List of extra labels to assign to docker on OAuth2 Proxy

#### Default value

```YAML
mariadb_exporter_extra_labels: []
```

### mariadb_exporter_extra_publish

List of extra port publishing for docker on OAuth2 Proxy

#### Default value

```YAML
mariadb_exporter_extra_publish: []
```

#### Example usage

```YAML
mariadb_exporter_extra_publish:
  - 127.0.0.1:9104:9104
```

### mariadb_exporter_image

Docker image to use for deployment on OAuth2 Proxy

#### Default value

```YAML
mariadb_exporter_image: prom/mysqld-exporter:v{{ mariadb_exporter_version }}
```

### mariadb_exporter_memory_limit

Memory limit with Docker deployment

#### Default value

```YAML
mariadb_exporter_memory_limit:
```

#### Example usage

```YAML
mariadb_exporter_memory_limit: 1024m
```

### mariadb_exporter_memory_soft_limit

Soft memory limit with Docker deployment

#### Default value

```YAML
mariadb_exporter_memory_soft_limit:
```

#### Example usage

```YAML
mariadb_exporter_memory_soft_limit: 512m
```

### mariadb_exporter_memory_swap

Swap usage with Docker deployment

#### Default value

```YAML
mariadb_exporter_memory_swap:
```

#### Example usage

```YAML
mariadb_exporter_memory_swap: 2048m
```

### mariadb_exporter_network

Optional docker network to attach on OAuth2 Proxy

#### Default value

```YAML
mariadb_exporter_network: '{{ mariadb_network }}'
```

### mariadb_exporter_number_of_cpus

Number of CPUs with Docker deployment

#### Default value

```YAML
mariadb_exporter_number_of_cpus:
```

#### Example usage

```YAML
mariadb_exporter_number_of_cpus: '1.5'
```

### mariadb_exporter_pull_image

Pull image as part of the tasks

#### Default value

```YAML
mariadb_exporter_pull_image: true
```

### mariadb_exporter_version

Version of the release to install

#### Default value

```YAML
mariadb_exporter_version: 0.18.0
```

### mariadb_extra_configs

Write additional config files

#### Default value

```YAML
mariadb_extra_configs: []
```

#### Example usage

```YAML
mariadb_extra_configs:
  - name: example
    priority: 50
    content: |
      foo1 = bar1
      foo2 = bar2
      foo3 = bar3
  - name: foobar
    state: absent
```

### mariadb_extra_databases

List of additional databases to create for native installation

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

### mariadb_extra_folders

List of extra folders to create

#### Default value

```YAML
mariadb_extra_folders: []
```

#### Example usage

```YAML
mariadb_extra_folders:
  - /path/to/host/folder1
  - /path/to/host/folder2
  - /path/to/host/folder3
```

### mariadb_extra_labels

List of extra labels to assign to docker

#### Default value

```YAML
mariadb_extra_labels: []
```

### mariadb_extra_publish

List of extra port publishing for docker

#### Default value

```YAML
mariadb_extra_publish: []
```

#### Example usage

```YAML
mariadb_extra_publish:
  - 127.0.0.1:3306:3306
```

### mariadb_extra_users

List of additional users to create for native installation

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

### mariadb_extra_volumes

List of extra volumes to mount for docker

#### Default value

```YAML
mariadb_extra_volumes: []
```

#### Example usage

```YAML
mariadb_extra_volumes:
  - /path/to/host/folder1:/path/within/container1
  - /path/to/host/folder2:/path/within/container2
  - /path/to/host/folder3:/path/within/container3
```

### mariadb_galera_address

Node address within galera cluster

#### Default value

```YAML
mariadb_galera_address: '{{ ansible_address }}'
```

### mariadb_galera_cluster

#### Default value

```YAML
mariadb_galera_cluster: galera
```

### mariadb_galera_enabled

Enable galera clustering

#### Default value

```YAML
mariadb_galera_enabled: false
```

### mariadb_galera_name

Node name within galera cluster

#### Default value

```YAML
mariadb_galera_name: '{{ inventory_hostname }}'
```

### mariadb_galera_nodes

Node addresses part of galera cluster

#### Default value

```YAML
mariadb_galera_nodes: []
```

### mariadb_galera_primary

Inventory of primary galera node

#### Default value

```YAML
mariadb_galera_primary:
```

### mariadb_global_databases

List of databases to create for native installation

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

List of users to create for native installation

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

### mariadb_image

Docker image to use for deployment

#### Default value

```YAML
mariadb_image: mariadb:{{ mariadb_upstream_version }}
```

### mariadb_innodb_buffer_pool_instances

InnoDB buffer pool instances

#### Default value

```YAML
mariadb_innodb_buffer_pool_instances: 1
```

### mariadb_innodb_buffer_pool_size

InnoDB buffer pool size

#### Default value

```YAML
mariadb_innodb_buffer_pool_size: 256M
```

### mariadb_innodb_file_per_table

InnoDB file per table

#### Default value

```YAML
mariadb_innodb_file_per_table: 1
```

### mariadb_innodb_flush_log_at_trx_commit

InnoDB flush at trx commit

#### Default value

```YAML
mariadb_innodb_flush_log_at_trx_commit: 1
```

### mariadb_innodb_io_capacity

InnoDB IO capacity

#### Default value

```YAML
mariadb_innodb_io_capacity: 1000
```

### mariadb_innodb_max_dirty_pages_pct

InnoDB max dirty pages percentage

#### Default value

```YAML
mariadb_innodb_max_dirty_pages_pct: 90
```

### mariadb_installation

Select installation method, could be native or docker

#### Default value

```YAML
mariadb_installation: native
```

### mariadb_key_buffer_size

Key buffer size

#### Default value

```YAML
mariadb_key_buffer_size: 32M
```

### mariadb_keyring

Path for the repository keyring

#### Default value

```YAML
mariadb_keyring: /usr/share/keyrings/mariadb-archive-keyring.gpg
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

### mariadb_memory_limit

Memory limit with Docker deployment

#### Default value

```YAML
mariadb_memory_limit:
```

#### Example usage

```YAML
mariadb_memory_limit: 1024m
```

### mariadb_memory_soft_limit

Soft memory limit with Docker deployment

#### Default value

```YAML
mariadb_memory_soft_limit:
```

#### Example usage

```YAML
mariadb_memory_soft_limit: 512m
```

### mariadb_memory_swap

Swap usage with Docker deployment

#### Default value

```YAML
mariadb_memory_swap:
```

#### Example usage

```YAML
mariadb_memory_swap: 2048m
```

### mariadb_network

Optional docker network to attach

#### Default value

```YAML
mariadb_network:
```

### mariadb_number_of_cpus

Number of CPUs with Docker deployment

#### Default value

```YAML
mariadb_number_of_cpus:
```

#### Example usage

```YAML
mariadb_number_of_cpus: '1.0'
```

### mariadb_oom_score_adjust

Adjustment score for OOM killer

#### Default value

```YAML
mariadb_oom_score_adjust: -999
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
  - rsync
```

### mariadb_password

Password used within docker deployment

#### Default value

```YAML
mariadb_password:
```

### mariadb_pull_image

Pull image as part of the tasks

#### Default value

```YAML
mariadb_pull_image: true
```

### mariadb_query_cache_size

Query cache size

#### Default value

```YAML
mariadb_query_cache_size: 0
```

### mariadb_query_cache_type

Query cache type

#### Default value

```YAML
mariadb_query_cache_type: 0
```

### mariadb_root_hosts

Allowed hosts for root user

#### Default value

```YAML
mariadb_root_hosts:
  - localhost
  - 127.0.0.1
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

### mariadb_skip_name_resolve

Skip name resolving

#### Default value

```YAML
mariadb_skip_name_resolve: true
```

### mariadb_symbolic_links

Symbolic links

#### Default value

```YAML
mariadb_symbolic_links: 0
```

### mariadb_temp_directory

Temporary directory used by MariaDB

#### Default value

```YAML
mariadb_temp_directory:
```

### mariadb_timeout_start_sec

Time to wait for daemon startup

#### Default value

```YAML
mariadb_timeout_start_sec: 120
```

### mariadb_upstream_arch

Upstream repo architecture

#### Default value

```YAML
mariadb_upstream_arch: "{{ 'arm64' if ansible_architecture == 'aarch64' else 'amd64'
  }}"
```

### mariadb_upstream_mirror

Upstream repo mirror URL

#### Default value

```YAML
mariadb_upstream_mirror: http://mirror.23m.com/mariadb/repo
```

### mariadb_upstream_repo

Install from upstream repository

#### Default value

```YAML
mariadb_upstream_repo: true
```

### mariadb_upstream_version

Upstream repo version

#### Default value

```YAML
mariadb_upstream_version: 11.8
```

### mariadb_username

Username used within docker deployment

#### Default value

```YAML
mariadb_username:
```

## Discovered Tags

**_mariadb_**

**_mariadb-exporter_**

## Dependencies

- [rolehippie.docker](https://github.com/rolehippie/docker)
- [community.docker](https://github.com/ansible-collections/community.docker)
- [community.mysql](https://github.com/ansible-collections/community.mysql)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)

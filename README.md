# mariadb

[![Build Status](https://cloud.drone.io/api/badges/rolehippie/mariadb/status.svg)](https://cloud.drone.io/rolehippie/mariadb)

Ansible role to configure mariadb

## Table of content

* [Default Variables](#default-variables)
  * [mariadb_character_set_server](#mariadb_character_set_server)
  * [mariadb_collation_server](#mariadb_collation_server)
  * [mariadb_cron_enabled](#mariadb_cron_enabled)
  * [mariadb_default_character_set](#mariadb_default_character_set)
  * [mariadb_general_db](#mariadb_general_db)
  * [mariadb_general_password](#mariadb_general_password)
  * [mariadb_general_username](#mariadb_general_username)
  * [mariadb_image](#mariadb_image)
  * [mariadb_innodb_buffer_size](#mariadb_innodb_buffer_size)
  * [mariadb_innodb_log_file_size](#mariadb_innodb_log_file_size)
  * [mariadb_log_bin](#mariadb_log_bin)
  * [mariadb_max_allowed_packet](#mariadb_max_allowed_packet)
  * [mariadb_max_connections](#mariadb_max_connections)
  * [mariadb_network](#mariadb_network)
  * [mariadb_publish](#mariadb_publish)
  * [mariadb_publish_server](#mariadb_publish_server)
  * [mariadb_root_password](#mariadb_root_password)
  * [mariadb_volume_backup](#mariadb_volume_backup)
  * [mariadb_volume_server](#mariadb_volume_server)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### mariadb_character_set_server

Character set server

#### Default value

```YAML
mariadb_character_set_server: utf8mb4
```

### mariadb_collation_server

Collation server

#### Default value

```YAML
mariadb_collation_server: utf8mb4_unicode_ci
```

### mariadb_cron_enabled

Enable integrated cronjob

#### Default value

```YAML
mariadb_cron_enabled: false
```

### mariadb_default_character_set

Default character set

#### Default value

```YAML
mariadb_default_character_set: utf8mb4
```

### mariadb_general_db

Database to create on start

#### Default value

```YAML
mariadb_general_db:
```

### mariadb_general_password

Password for general user

#### Default value

```YAML
mariadb_general_password:
```

### mariadb_general_username

Username for general user

#### Default value

```YAML
mariadb_general_username:
```

### mariadb_image

Docker image to use

#### Default value

```YAML
mariadb_image: webhippie/mariadb:latest
```

### mariadb_innodb_buffer_size

Innodb buffere size

#### Default value

```YAML
mariadb_innodb_buffer_size: 1G
```

### mariadb_innodb_log_file_size

Innodb log file size

#### Default value

```YAML
mariadb_innodb_log_file_size: 64M
```

### mariadb_log_bin

MariaDB log bin

#### Default value

```YAML
mariadb_log_bin: 0
```

### mariadb_max_allowed_packet

Max allowed packet size

#### Default value

```YAML
mariadb_max_allowed_packet: 128M
```

### mariadb_max_connections

Max allowed connections

#### Default value

```YAML
mariadb_max_connections: 250
```

### mariadb_network

Docker network to connect to

#### Default value

```YAML
mariadb_network:
```

#### Example usage

```YAML
mariadb_network: traefik
```

### mariadb_publish

Publish the service on that binding

### mariadb_publish_server

#### Default value

```YAML
mariadb_publish_server: 127.0.0.1:3306
```

### mariadb_root_password

Password for root user

#### Default value

```YAML
mariadb_root_password:
```

### mariadb_volume_backup

Path to backup volume

#### Default value

```YAML
mariadb_volume_backup: /var/lib/backup
```

### mariadb_volume_server

Path to server volume

#### Default value

```YAML
mariadb_volume_server: /var/lib/mariadb
```

## Dependencies

* [docker](https://github.com/rolehippie/docker)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)

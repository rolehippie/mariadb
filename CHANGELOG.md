# Changelog

## [2.2.0](https://github.com/rolehippie/mariadb/compare/v2.1.0...v2.2.0) (2025-03-03)


### Features

* **deps:** update dependency prometheus/mysqld_exporter to v0.17.1 ([#33](https://github.com/rolehippie/mariadb/issues/33)) ([dab64ca](https://github.com/rolehippie/mariadb/commit/dab64ca9ecc675943079bcfa52551bda0ee59f95))
* upgrade upstream repo to 11.8 ([8db20eb](https://github.com/rolehippie/mariadb/commit/8db20eb99f49453211d3147b153bc970f9b22202))


### Bugfixes

* **deps:** update dependency prometheus/mysqld_exporter to v0.17.2 ([#34](https://github.com/rolehippie/mariadb/issues/34)) ([ecd0957](https://github.com/rolehippie/mariadb/commit/ecd0957b478f66e69fa93fd8013d84d2b3408109))

## [2.1.0](https://github.com/rolehippie/mariadb/compare/v2.0.0...v2.1.0) (2024-11-11)


### Features

* **deps:** update dependency prometheus/mysqld_exporter to v0.16.0 ([#30](https://github.com/rolehippie/mariadb/issues/30)) ([5ed31b3](https://github.com/rolehippie/mariadb/commit/5ed31b34562591adbac0aad2157aebe0097dbe98))

## [2.0.0](https://github.com/rolehippie/mariadb/compare/v1.3.1...v2.0.0) (2024-02-12)


### Features

* drop support for ubuntu 18.04 ([691a8aa](https://github.com/rolehippie/mariadb/commit/691a8aa918b75f92f87fa24a18d9ded73a4eeb3a))
* used full qualified collection names ([a67a856](https://github.com/rolehippie/mariadb/commit/a67a856085bc7f5e431f0c5f2256c3d4a43492ff))


### Bugfixes

* remove meta requirements and document used collections ([fbb78b4](https://github.com/rolehippie/mariadb/commit/fbb78b4ad6a65bfe3160266b1440abd60a690052))

## [1.3.1](https://github.com/rolehippie/mariadb/compare/v1.3.0...v1.3.1) (2023-12-18)


### Bugfixes

* **deps:** update dependency prometheus/mysqld_exporter to v0.15.1 ([e950298](https://github.com/rolehippie/mariadb/commit/e9502986fa0debc694bb8585a22679cc1660b312))

## [1.3.0](https://github.com/rolehippie/mariadb/compare/v1.2.0...v1.3.0) (2023-11-20)


### Features

* integrate docker deployment and upgrade to 11.1 ([3977fad](https://github.com/rolehippie/mariadb/commit/3977fad256f0467ef67eb986c57517117331c52f))

## [1.2.0](https://github.com/rolehippie/mariadb/compare/v1.1.0...v1.2.0) (2023-06-26)


### Features

* **deps:** update dependency prometheus/mysqld_exporter to v0.15.0 ([2394977](https://github.com/rolehippie/mariadb/commit/239497763e61f90f9971cc5f8fa622ec36974680))

## [1.1.0](https://github.com/rolehippie/mariadb/compare/v1.0.0...v1.1.0) (2023-04-17)


### Features

* use unified path for repo key and drop legacy key ([7e99834](https://github.com/rolehippie/mariadb/commit/7e998340b514468431754f23f7042c18257a5d4a))

## 1.0.0 (2023-01-05)


### Features

* add option to write config files ([31bbfba](https://github.com/rolehippie/mariadb/commit/31bbfba420119c47dff84030b898d4b8f9e52f4e))
* integrate galera cluster creation ([fa5e075](https://github.com/rolehippie/mariadb/commit/fa5e075bc379ad833e883580b05c1b403c2c580a))
* restructure workflows and enable automated releases ([7e740d6](https://github.com/rolehippie/mariadb/commit/7e740d6274a00e1c29f9a72e59e5a4c4277e7373))


### Bugfixes

* add dummy default for delegate_to ([03db5c8](https://github.com/rolehippie/mariadb/commit/03db5c880a6fa199cde3c8ae71218507cd0ca510))
* delegate to inventory_hostname if not galera ([db4827f](https://github.com/rolehippie/mariadb/commit/db4827f22da521712c24b457232f14939ff15271))
* stdout and stderr for exporter version check ([cbc36f6](https://github.com/rolehippie/mariadb/commit/cbc36f695c9afe479df56a2353f523ff40690e96))
* switch to working mirror, make mirror configurable ([d9782bb](https://github.com/rolehippie/mariadb/commit/d9782bb3ff4ea9c084762fd157a28a14b6c90b62))
* use include_tasks instead of include ([f0dd84d](https://github.com/rolehippie/mariadb/commit/f0dd84dff0dfd723bf82a975c7e7d8b27a215647))

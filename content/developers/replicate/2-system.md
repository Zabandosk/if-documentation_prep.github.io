# System requirements

This section describes the system requirements implemented in the Imagining Futures Repository. We used two different virtual machines, one for the database and other for the application. Both virtual machines share very similar features. This document will point out the differences between them.

## Server

| Feature   |      Details      |      Required      |
|----------|:-------------:|:-------------:|
| Operating System |  Ubuntu 20.04 (LTS) x64 | Linux, Mac OS X 10.9+, or Windows Server 2012+ |
| Memory |    4Gb   | 4Gb or more |
| Storage | 80Gb disk | N/A |
| Processor | 2 vCPUs | 2 vCPUs or more |

## Service

We opted for Digital Ocean to host the virtual machines. Basic configuration for both virtual machines is described below.

| Feature   |      Installed      |
|----------|:-------------:|
| Type |  Standard Droplet |
| Image |    Ubuntu 20.04 (LTS) x64   |
| Size | 4Gb/2vCPUs |
| Storage | 80Gb disk |
| Region | LON1 |

Storage of files is done in a Digital Ocean Space. The space is configured to be accessible only from the virtual machines.

## Core software

| Feature   |      Details      |     Minimum      |
|----------|:-------------:|:-------------:|
| Webserver |  Apache 2.4 | Apache 2.4 |
| PHP |    8.2   | 7.4 |

## Required and Suggested Software Packages

The following packages and php modules were installed in the virtual machine that host the packages, following the instructions from [CA documentation](https://manual.collectiveaccess.org/providence/user/setup/systemReq.html#required-and-suggested-software-packages-by-distribution).

```bash
wget zip curl dcraw ffmpeg git-all ghostscript imagemagick libapache2-mod-php8.2 libreoffice mysql-client php8.2 php8.2-curl php8.2-gd php8.2-intl php8.2-xml php8.2-zip php8.2-bcmath php8.2-mysql php8.2-mysqlnd php8.2-fileinfo php8.2-gmagick php8.2-opcache php8.2-mbstring
```

We skipped the installation of the php-process module, since there's no such module in Ubuntu 20.04.

## Database


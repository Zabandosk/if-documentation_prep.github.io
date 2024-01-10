# System requirements

This section describes the system requirements implemented in the Imagining Futures Repository. We used two different virtual machines, one for the database and other for the application. Both virtual machines share very similar features. This document will point out the differences between them.

## Server

- [Application server](#application-server)

| Feature   |      Details      |      Required      |
|----------|:-------------:|:-------------:|
| Operating System |  Ubuntu 22.04 (LTS) x64 | Linux, Mac OS X 10.9+, or Windows Server 2012+ |
| Memory |    8Gb   | 4Gb or more |
| Storage | 80Gb disk | N/A |
| Processor | 4 vCPUs | 2 vCPUs or more |

**Note:** This configuration is the minimun to work with ElasticSearch. If you don't need ElasticSearch, you can use a virtual machine with 4Gb of memory and 2 vCPUs.

- [Database server](#database-server)

| Feature   |      Details      |      Required      |
|----------|:-------------:|:-------------:|
| Operating System |  Ubuntu 20.04 (LTS) x64 | Linux, Mac OS X 10.9+, or Windows Server 2012+ |
| Memory |    4Gb   | 4Gb or more |
| Storage | 80Gb disk | N/A |
| Processor | 2 vCPUs | 2 vCPUs or more |

## Core software

| Feature   |      Details      |     Minimum      |
|----------|:-------------:|:-------------:|
| Webserver |  Apache 2.4 | Apache 2.4 |
| PHP |    8.2   | 7.4 |
| Database | MySQL 8.0 | MySQL 5.7 |

## Required and Suggested Software Packages

The following packages and php modules were installed in the virtual machine that host the packages, following the instructions from [CA documentation](https://manual.collectiveaccess.org/providence/user/setup/systemReq.html#required-and-suggested-software-packages-by-distribution).

```bash
wget zip curl dcraw ffmpeg git-all ghostscript imagemagick libapache2-mod-php8.2 libreoffice \
 mysql-client php8.2 php8.2-curl php8.2-gd php8.2-intl php8.2-xml php8.2-zip php8.2-bcmath \
 php8.2-mysql php8.2-mysqlnd php8.2-fileinfo php8.2-gmagick php8.2-opcache php8.2-mbstring \
 php8.2-xmlrpc php8.2-posix php8.2-dev php8.2-redis php8.2-gmp
```

We skipped the installation of the php-process module, as is pointed out in CA documentation, since there's no such module in Ubuntu 22.04.

### Composer

As we're working with a development version of CollectiveAccess, we need to install Composer. We followed the instructions from [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-composer-on-ubuntu-20-04).

## Database

We're using a separate server to host our database. In that way, we can control the disk space, the memory and the processor of the database server independently of the application server. This is an important decission, since the database server is the most demanding in terms of memory and processor.

We installed Mysql Server version: 8.0.33-0ubuntu0.20.04.1 (Ubuntu) in the database server. The database server is configured to accept connections only from the application server. Before launching the application to production, it is important to reinforce the security of the database server to avoid unauthorized access.

## Fail2ban

We installed Fail2ban in the application server to avoid brute force attacks. We followed the instructions from [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-protect-ssh-with-fail2ban-on-ubuntu-20-04).

## Redis-server

Redis is used to cache the results of the search engine. Installation is very straightforward, just follow the instructions from [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04).

Redis php8.2 extension is needed. Use the following command and restart Apache:

```bash
sudo apt-get install php-redis
```

## Install GraphicsMagick from source

We need to install GraphicsMagick from source to enable the support for the HEIC format. We followed the instructions from [GraphicsMagick](http://www.graphicsmagick.org/INSTALL-unix.html#install-unix).

We choose version 1.3.38, but newer versions can also be used.

```bash
wget https://sourceforge.net/projects/graphicsmagick/files/graphicsmagick/1.3.38/GraphicsMagick-1.3.38.tar.gz
tar -xvf GraphicsMagick-1.3.38.tar.gz
cd GraphicsMagick-1.3.38
./configure  --build x86_64-linux-gnu --enable-shared --enable-static --enable-libtool-verbose --prefix=/usr --mandir=${prefix}/share/man --infodir=${prefix}/share/info --docdir=${prefix}/share/doc/graphicsmagick --with-gs-font-dir=/usr/share/fonts/type1/gsfonts
make
sudo make install
```

`configure` options are the same as the ones used in the Ubuntu package.

## Aditional custom configuration

### Domain name

We used a domain name to access the application. This is not mandatory, but it is highly recommended.

Regarding CollectiveAccess configuration, the domain only needs to be declared in the `navbar-toggle` from `views/pageFormat/pageHeader.php` file of pawtucket2 theme.

### SSL certificate

It is highly recommended to use a SSL certificate to secure the communication between the users and the application. We used a free certificate from [Let's Encrypt](https://letsencrypt.org/). To make the configuration more easy, the certificate is issued using the [Certbot](https://certbot.eff.org/) tool. The certificate is configured to be renewed automatically.

### Email configuration

As this configuration depends on the email provider, we're not going to describe it here. Options like Gmail, osr other free providers don't work, since they require a two-step authentication.

We used SendGrid, as is the one recommended by CollectiveAccess developers, and multiple projects have been using it. CollectiveAccess documentation is not available. Some guidance can be found in this two forum posts: [Using SendGrid from SMTP to share records in Pawtucket fails](https://collectiveaccess.org/support/index.php?p=/discussion/301431/using-sendgrid-from-smtp-to-share-records-in-pawtucket-fails) and [Email configuration settings](https://collectiveaccess.org/support/index.php?p=/discussion/301146/email-configuration-settings).


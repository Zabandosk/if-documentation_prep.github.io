# Providence and Pawtucket2 Installation

Standard installation instructions for Providence and Pawtucket2 are available in the [Collective Access documentation](https://manual.collectiveaccess.org/providence/user/setup/installation.html). The following instructions are specific to the installation of the forked codebase, which follows the [Installing development versions](https://github.com/ImaginingFutures/providence#installing-development-versions) instructions from the Imagining Futures Providence Github repository. Pawtucket2 installation is similar to Providence, so we will only point out the differences.

## Repositories

Clone the forked repositories:

```bash
git clone --depth 1 --branch dev/php8 https://github.com/ImaginingFutures/providence.git /var/www/html/ifrepo-admin
git clone --depth 1 --branch dev/php8 https://github.com/ImaginingFutures/pawtucket2.git /var/www/html/ifrepo
```

## Configuration

- Installation profile: \[Standard\] ISAD(G) - General Standard Archival Description

## Media folders

It's possible that the media folders are not created automatically. If that's the case, create the following folders:

```bash
mkdir /var/www/html/ifrepo-admin/media/collectiveaccess
mkdir /var/www/html/ifrepo-admin/media/collectiveaccess/images
mkdir /var/www/html/ifrepo-admin/media/collectiveaccess/tilepics
mkdir /var/www/html/ifrepo-admin/media/collectiveaccess/workspace
mkdir /var/www/html/ifrepo-admin/media/collectiveaccess/flv
mkdir /var/www/html/ifrepo-admin/media/collectiveaccess/quicktime
mkdir /var/www/html/ifrepo-admin/media/collectiveaccess/windowsmedia
mkdir /var/www/html/ifrepo-admin/media/collectiveaccess/swf
mkdir /var/www/html/ifrepo-admin/media/collectiveaccess/mp3
```

All folder must have the following permissions:

```bash
chown -R www-data:www-data /var/www/html/ifrepo-admin/media/collectiveaccess
```

As the media files are the same for both Providence and Pawtucket2, we can create a symbolic link to the media folder in the Pawtucket2 installation:

```bash
ln -s /var/www/html/ifrepo-admin/media/collectiveaccess /var/www/html/ifrepo/media/collectiveaccess
```

Other folders that need permissions:

```bash
chown -R www-data:www-data /var/www/html/ifrepo-admin/app/tmp
chown -R www-data:www-data /var/www/html/ifrepo-admin/app/log
chown -R /var/www/html/ifrepo-admin/vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache/Serializer
chmod -R 755 /var/www/html/ifrepo-admin/vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache/Serializer
```

It's possible that after installation some other folders needs to be created and/or permissions need to be changed. If that's the case, the installation process will let you know.

And that's it! You can now access to the Providence and Pawtucket2 installations.

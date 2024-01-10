# Web Application Deployment and Version Control Workflow

## Getting Started

This document provides an overview of the deployment workflow and version control strategy. While we've provided a specific setup, please note that this can be adapted to different systems based on your requirements.

### Workflow logic

Our workflow follows a straightforward logic:

- The remote system is the central repository, housing the primary, development, and `dev/php8` branches.
- The local system mirrors the remote repository and contains the main and development branches.
- The development branch is for testing new features and bug fixes. It's merged into the main branch for production deployment.
- The main branch is dedicated to deploying code to the production server. It is not updated directly but is updated through merges from the development branch.
- The `dev/php8` branch is used to test changes for the forked codebase and is also merged into the main branch for production.

### Branches

We use three main branches:

- `main`: Reserved for production code deployments, updated through merges from the development branch.
- `ifdev`:  For testing new features and bug fixes. Merged into main for production.
- `dev/php8`: For testing changes in the forked codebase. Merged into main for production.

### Workflow

Our workflow can be summarized as follows:

1. Clone the remote repository to your local system.
2. Create a new branch on the local system for testing new features and bug fixes.
3. Commit changes to this new branch.
4. Push the new branch to the remote repository.
5. Merge the new branch into the development branch.
6. Test new features and bug fixes in the development branch.
7. Merge the development branch into the main branch for production deployment.
8. Deploy the code to the production server.

### Policies

We have established the following policies:

- The `main` branch is never updated directly; it is updated by merging the development branch.
- Core code updates are merged into the `dev/php8` branch before being merged into `main`.
- Access to the remote repository is restricted. If others need access, they create their branches and request merges for deployment.

### Syncing the Remote and Local Systems

To ensure synchronization between local and remote systems, follow these policies:

- Fetch the main and development branches on your local system before committing changes to development.
- Core code updates are periodically merged into the dev/php8 branch. Be sure to fetch these updates to keep your local system up to date.

## Implement the Workflow

### On the Server

#### If application is not installed

1. **Clone the Repository and prepare permissions**

```bash
git clone --depth 1 --branch dev/php8 https://github.com/collectiveaccess/providence.git /var/www/html/ifrepo-admin

sudo chown -R imaginingfutures:imaginingfutures /var/www/html/ifrepo-admin
sudo chmod -R u+w /var/www/html/ifrepo-admin
```

2. **Create and Switch to the `main` Branch**

```bash
git checkout -b main
git branch -m main
```

3. **Install**

Follow the general installation instructions given in [install](../replicate/3-install.md).

4. **Edit .gitignore to Accept Changes in app/conf/local/**

```bash
nano /var/www/html/ifrepo-admin/.gitignore
```

Delete the following lines:

```bash
app/conf/local/*
```

5. **Commit Changes to the `main` Branch**

```bash
git add .
git commit -m "Tracking in main"
```

6. **Configure Receive Hooks**

```{admonition} Warning
:class: warning
Use with caution. This will overwrite any changes made to the server. Ensure that you have a strong update policy in place before proceeding. Also, ensure that the `main` branch is up to date with the `dev/php8` branch.
```

```bash
git config receive.denyCurrentBranch updateInstead
```

#### If application is already installed

1. **Backup Existing Application**

```bash
mv /var/www/html/ifrepo-admin /var/www/html/ifrepo-admin-safe
```

2. **Clone the Repository and Prepare Permissions**

```bash
git clone --depth 1 --branch dev/php8 https://github.com/collectiveaccess/providence.git /var/www/html/ifrepo-admin
sudo chown -R imaginingfutures:imaginingfutures /var/www/html/ifrepo-admin
sudo chmod -R u+w /var/www/html/ifrepo-admin
```

3. **Create and Switch to the main Branch**

```bash
git checkout -b main
git branch -m main
```

4. **Copy Necessary Files**

```bash
cp /var/www/html/ifrepo-admin-safe/setup.php /var/www/html/ifrepo-admin/setup.php
cp /var/www/html/ifrepo-admin-safe/app/conf/app.conf /var/www/html/ifrepo-admin/app/conf/local/app.conf
cp /var/www/html/ifrepo-admin-safe/app/conf/global.conf /var/www/html/ifrepo-admin/app/conf/local/global.conf
cp /var/www/html/ifrepo-admin-safe/app/conf/datetime.conf /var/www/html/ifrepo-admin/app/conf/local/datetime.conf
cp /var/www/html/ifrepo-admin-safe/app/conf/external_applications.conf /var/www/html/ifrepo-admin/app/conf/local/external_applications.conf
cp /var/www/html/ifrepo-admin-safe/app/conf/navigation.conf /var/www/html/ifrepo-admin/app/conf/local/navigation.conf
cp /var/www/html/ifrepo-admin-safe/app/lib/Parsers/TimeExpressionParser.php /var/www/html/ifrepo-admin/app/lib/Parsers/TimeExpressionParser.php
cp /var/www/html/ifrepo-admin-safe/composer.json /var/www/html/ifrepo-admin/composer.json
```

5. **Install Composer Dependencies**

```bash
composer install --no-dev --optimize-autoloader --working-dir=/var/www/html/ifrepo-admin
```

6. **Create Symlink for Media (depending of your original installation)**

```bash
sudo ln -s /mnt/s3storage /var/www/html/ifrepo-admin/media
```

7. **Set Permissions and Ownership**

```bash
chown -R www-data:www-data /var/www/html/ifrepo-admin/media/
chown -R www-data:www-data /var/www/html/ifrepo-admin/app/tmp
chown -R www-data:www-data /var/www/html/ifrepo-admin/app/log
chown -R www-data:www-data /var/www/html/ifrepo-admin/uploads
chmod -R 755 /var/www/html/ifrepo-admin/media
chmod -R 755 /var/www/html/ifrepo-admin/app/tmp
chmod -R 755 /var/www/html/ifrepo-admin/app/log
chmod -R 755 /var/www/html/ifrepo-admin/uploads
```

8. **Copy HTMLPurifier Definitions**

```bash
cp -r /var/www/html/ifrepo-admin-safe/vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache /var/www/html/ifrepo-admin/vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache
chown -R www-data:www-data /var/www/html/ifrepo-admin/vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache
chmod -R 755 /var/www/html/ifrepo-admin/vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache
```

9. **Remove Backup Directory**

```bash
rm -rf /var/www/html/ifrepo-admin-safe
```

10. **Edit .gitignore to Accept Changes in app/conf/local/**

```bash
nano /var/www/html/ifrepo-admin/.gitignore
```

Delete the following lines:

```bash
app/conf/local/*
```

11. **Commit Changes to the `main` Branch**

```bash
git add .
git commit -m "Tracking in main"
```

12. **Configure Receive Hooks**

```{admonition} Warning
:class: warning
Use with caution. This will overwrite any changes made to the server. Ensure that you have a strong update policy in place before proceeding. Also, ensure that the `main` branch is up to date with the `dev/php8` branch.
```

```bash
git config receive.denyCurrentBranch updateInstead
```

### On the Local Machine

1. **Clone the Repository**

```bash
git clone root@157.245.30.79:/var/www/html/ifrepo-admin/.git ifrepo-admin
```

2. **Set Permissions and Ownership**

```bash
sudo chown -R imaginingfutures:imaginingfutures /var/www/html/ifrepo-admin
sudo chmod -R u+w /var/www/html/ifrepo-admin
```

3. **Create and Switch to the `ifdev` Branch**

```bash
git checkout -b ifdev
```

4. **Install Composer Dependencies**

```bash
composer install --no-dev --optimize-autoloader --working-dir=/var/www/html/ifrepo-admin
```

5. **Set Permissions and Ownership**

```bash
chown -R www-data:www-data /var/www/html/ifrepo-admin/media/
chown -R www-data:www-data /var/www/html/ifrepo-admin/app/tmp
chown -R www-data:www-data /var/www/html/ifrepo-admin/app/log
chown -R www-data:www-data /var/www/html/ifrepo-admin/uploads
chmod -R 755 /var/www/html/ifrepo-admin/media
chmod -R 755 /var/www/html/ifrepo-admin/app/tmp
chmod -R 755 /var/www/html/ifrepo-admin/app/log
chmod -R 755 /var/www/html/ifrepo-admin/uploads
```

6. **Set Permissions and Ownership for HTMLPurifier Definitions**

```bash
chown -R www-data:www-data /var/www/html/ifrepo-admin/vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache
chmod -R 755 /var/www/html/ifrepo-admin/vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache
```

7. **Install**

Follow the general installation instructions given in [install](../replicate/3-install.md).

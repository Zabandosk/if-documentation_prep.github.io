# Providence and Pawtucket2 Installation

Standard installation instructions for Providence and Pawtucket2 are available in the [Collective Access documentation](https://manual.collectiveaccess.org/providence/user/setup/installation.html). The following instructions are specific to the installation of the forked codebase, which follows the [Installing development versions](https://github.com/ImaginingFutures/providence#installing-development-versions) instructions from the Imagining Futures Providence Github repository. Pawtucket2 installation is similar to Providence, so we will only point out the differences.

## Repositories

Clone the forked repositories:

```bash
git clone --depth 1 --branch if-providence https://github.com/ImaginingFutures/providence.git /var/www/html/ifrepo-admin
git clone --depth 1 --branch if-pawtucket https://github.com/ImaginingFutures/pawtucket2.git /var/www/html/ifrepo
```


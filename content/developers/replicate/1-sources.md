# Collective Access Codebase Strategy

In pursuit of the long-term sustainability of the codebase for this project, we've devised a strategic approach. Firstly, we've chosen to fork the Collective Access codebase, enabling us to implement and track our modifications while maintaining synchronization with the main Collective Access codebase.

Another crucial decision pertains to the selection of  [PHP 8.2](https://www.php.net/releases/8.2/en.php) for the project. This choice is aimed at enhancing our ability to manage future updates to the Collective Access codebase. Additionally, the utilization of PHP 8 brings about noteworthy advancements in terms of speed, security, and efficiency. Consequently, we've opted to employ a release candidate version of Collective Access instead of the latest stable version (1.7.16 - June 25, 2022), which lacks PHP 8 support.

## Branch structure

We've established two distinct branches within the Collective Access codebase: `if-providence` and `if-pawtucket`. The former encompasses modifications related to the Providence component, while the latter houses changes associated with the Pawtucket component of the Collective Access framework [^1].

Both `if-providence` and `if-pawtucket` branches are built upon the `dev/php8` branch of the Collective Access codebase. This particular branch represents a release candidate for the upcoming Providence and Pawtucket2 (2.0) versions.

You can find the original branches at the following locations:

```
Providence: https://github.com/ImaginingFutures/providence/tree/if-providence
Pawtucket2: https://github.com/ImaginingFutures/pawtucket2/tree/if-pawtucket
```


## Notes

[^1]: The Collective Access codebase is divided into two components: Providence and Pawtucket. Providence is the backend component, which is responsible for the management of the data. Pawtucket is the frontend component, which is responsible for the presentation of the data. See [Collective Access documentation](https://manual.collectiveaccess.org/intro/whatIs.html) for more information.

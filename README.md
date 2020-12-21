# IoTHM

[![Unit Tests]]
[![System Tests]]
[![Lint]]
[![codecov]]

**[WiP]**

The IoTHM is a distributed data-driven IoT platform which combines information
from different hardware sensors applied to home monitoring. The goal is to
support embedded platforms such as ESP32 to monitor aspects like temperature,
humidity, pressure and so on, and make the information available to be easily
accessed and analyzed by using dashboards or even processed my Machine Learning
models.

This is a open-source project based on many tools such as: Docker, Python,
Django, PostgreSQL, Redis, Elasticsearch and so on. Here are the services which
are part of the IoTHM:

* [Events REST API, provides access to the monitoring data in a form of a REST API](./Events%20REST%20API/README.md)
* [Events Database, database containing all the monitoring data](./Events%20Database/README.md)
* [Monitoring, centralized platform's log monitoring](./Monitoring/README.md)
* [Sensoring, reads and sends the data from the hardware sensors to be processed](./Sensoring/README.md)

Detailed information about each service will be provided inside the respective
folders.

## Running

To build and run the application, clone the repository and run in a terminal
from the same directory where the ```docker-compose-{environment}.yaml``` file
is, where *environment* can be *dev*, *test*, *prod* or whatever:

```shell
$ docker-compose -f docker-compose-dev.yaml up
```

To stop the application, run from the same directory:

```
$ docker-compose stop
```

## Accessing

Each service is exposed through a specific port, after build and run it's
possible to access the following:

* Data REST API, port 8000
* Elasticsearch, port 9200
* Kibana, port 5601
* PostgreSQL Database, port 5432

Detailed information about each service will be provided inside the respective
folders.

## Monitoring

All the logs are sent to an Elasticsearch instance. The main goal here is to
provide a real time log stream that can be monitored using Kibana.

## Testing

The file ```docker-compose-test.yaml``` runs unit and system tests generating
the reports after that.

```shell
$ docker-compose -f docker-compose-test.yaml up
```

This should start the container, run the tests, generate the reports and exit.

## Development

### Branching

The ```main``` is a **regular branch** which always contains the latest
**stable** codebase and must **never** be broken.

The ```develop``` is a **regular branch** which always contains the latest
**development** codebase and **eventually** can be broken. But you'll need to
accept the **sombrero of shame** if you do that.

The ```release``` is a **regular branch** which contains a specific release
version. You must use the following name convention: **release-X.Y.Z**, where
X, Y and Z are: major, minor and patch [version numbers](#versioning).

The ```experimental``` is a **temporary branch** which contains a new feature or
ideia that is not part of a release or sprint. You must use the following name
convention: **experimental-brief-description**.

The ```feature``` is a **temporary branch** which contains a new feature under
development that latter will be merged against the development branch. You must
use the following name convention: **feature-iothm-999-brief-description**,
where iothm-999 **must** correspond to a existing numbered task on the [project board](https://github.com/furansa/iothm/projects).

The ```bugfix``` is a **temporary branch** which contains necessary fix to be
applied **after** a specific release to be merged against the development branch.
You must use the following name convention: **bugfix-iothm-999-brief-description**,
where iothm-999 **must** correspond to a existing numbered task on the [project board](https://github.com/furansa/iothm/projects).

The ```hotfix``` is a **temporary branch** which contains a critical fix to be
applied **immediately** and merged against the main and the development branches.
You must use the following name convention: **hotfix-iothm-999-brief-description**,
where iothm-999 **must** correspond to a existing numbered task on the [project board](https://github.com/furansa/iothm/projects).

Feel free to apply the labels from GitHub to the branches, they are very helpful.

### Versioning

The project uses the [bump2version](https://pypi.org/project/bump2version) in
order to control the version numbers following the [semantic versioning 2.0.0](https://semver.org).

#### How to increment the version

**After commit a modification** (because the repository must be clean), you
must update the version according to the following rules:

* Increment the ```MAJOR``` version when you make incompatible API changes.
* Increment the ```MINOR``` version when you add functionality in a backwards compatible manner.
* Increment the ```PATCH``` version when you make backward compatible bug fixes.

It's possible to perform a dry-run test without touch any file, for example with
a ```MINOR```, run:

```shell
$ bump2version --dry-run --verbose minor
```

To increment the `MAJOR` version run:

```shell
$ bump2version major --commit
```

To increment the `MINOR` version run:

```shell
$ bump2version minor --commit
```

To increment the `PATCH` version run:

```shell
$ bump2version patch --commit
```

Then you can go ahead and commit again to send the updated versioning files.

### Commiting

The ```main```, ```develop``` and ```release``` branches have protection rules
against **push**.

In order to contribute you must create a new branch following the [branching](#branching)
guideline and once your work is done, open a **pull request** from your branch
to the **develop** branch.

The **pull request** will trigger the unit and system test suites automatically
and the code must **pass all the tests** and also be reviewed and approved by
at least one team member before merged in the **develop** branch (or even ``main``
or ``release`` in case of a ``*fix``).

Feel free to apply the labels from GitHub to the pull requests, they are very helpful.

This project uses **pipenv** and **pre-commit** in order to run some static
checks and formatting on the code. After clone the repository you need to create
a new **virtual environment** and install the dependencies:

```shell
$ pipenv shell
$ pipenv install --dev
$ pre-commit install
```

Every time you run the ```git commit``` command the code will be checked. To
run the checking manually, run:

```shell
$ pre-commit run --all-files
```

## References

* [The Twelve-Factor App](https://12factor.net)


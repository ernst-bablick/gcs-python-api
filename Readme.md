# Gridware Cluster Scheduler - Python API

(WORK IN PROGRESS) - Does not work with OCS in current state!

This is a Python API for Gridware Cluster Scheduler (GCS) (former Sun Grid Engine / Univa Grid Engine) that allows you to interact with GCS via the Python programming language. In difference to other APIs that usually wrap command line tools, this API directly accesses the primary C/C++ interface of GCS.

This allows for a more efficient and direct interaction from outside GCS (as a client) but also from within GCS (as a plugin or embedded module).

Currently, the API is just a set of tests that demonstrate the functionality. The API is implemented as C++ extension module for Python using the pybind11 library.

In future the API will be extended to cover following areas:

* Control API (start/stop/restart GCS components)
* Configuration API (manage GCS configuration)
* Job API (compatible to the DRMAA v2 API)
* Cluster Status API (monitoring of cluster status)
* Accounting API (manage and query accounting data)

## Dependencies

This API depends on packages mentioned in the `requirements.txt` file. You can install them via pip.

Additionally you need to install the pybind development package for your system in order to build the C++ bindings. For example, on Ubuntu/Debian you can install it via:

```bash
sudo apt-get install pybind11-dev
```

The ocs directory has to contain a file named ocs_bridge.so that provides the C++ interface to GCS. This file is usually part of the GCS installation when it is built with Python support. You can copy it from there or link it via a symbolic link. Make sure that the file is compatible with your GCS version and running qmaster.

Before you run the tests, make sure that your environment is set up correctly:

* LD_PRELOAD=./ocs/ocs_bridge.so - is required to load the C++ extension module
* SGE_ROOT=<Path to GCS installation> - is required to find GCS distribution files
* SGE_QMASTER_PORT=<Port of GCS qmaster> - is required to connect to the GCS qmaster

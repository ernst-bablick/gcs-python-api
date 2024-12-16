# Gridware Cluster Scheduler - Python API

This is the official Python API for Gridware Cluster Scheduler (GCS) (former Sun Grid Engine / Uniiva Grid Engine) that allows you to interact with GCS via the Python programming language. In difference to other APIs that usually wrap command line tools, this API directly accesses the primary C/C++ interface of GCS.

This allows for a more efficient and direct interaction from outside GCS (as a client) but also from within GCS (as a plugin or embedded module).

The interface functionality covers the following areas:

* Configuration API
* Job API (compatible to the DRMAA v2 API)
* Cluster Status API

Please be aware that gcs-api is still work in progress and not yet feature complete. The API is currently being developed and tested with GCS 9.x.x. Target for the development team is it to have a stable version of the API, that covers Configuration and Job management, with the release of GCS 10.0.0.


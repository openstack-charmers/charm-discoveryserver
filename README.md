# Etcd Discovery Server

## Description

This charm deploys the etcd discovery service, equivalent to discovery.etcd.io.

## Usage

An all-in-one discovery server is configured simply by deploying this charm.
To try it out:

```console
$ juju deploy --channel edge discoveryserver
$ curl http://<discoveryserver-address>:8087/new?size=3
```

## Relations

This charm currently contains no relations.

## Contributing

Please make pull requests.


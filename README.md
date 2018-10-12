# signalfx_api
Samples of working with the SignalFx API

Currently this is simply a couple of scripts to retrieve dashboards for local editing and to deploy a locally edited dashboard (as a new dashboard).

## Prerequisites
* A [SignalFx](https://signalfx.com/) account and an API token
* Python requests module

## Getting started
Edit `credentials.py` to contain your SignalFx API token.

## Retrieving dashboards
Edit `retrieve.py` to contain the dashboard ID to clone, then `python retrieve.py`.  A new directory will be created, named after the name of the dashboard you retrieved.  It will contain a JSON file describing the dashboard and a `charts` directory containing JSON objects for each associated chart.

## Deploying dashboards
Edit `deploy.py` to point to the name of the local directory containing the dashboard and charts, then `python deploy.py`.  All the charts in the directory will be created on SignalFx, followed by a dashboard with those charts.  The new dashboard ID will be returned.

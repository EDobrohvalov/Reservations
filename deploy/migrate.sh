#!/usr/bin/env bash

podman-compose --env-file ".$1-migration.env" up -d db-migrate
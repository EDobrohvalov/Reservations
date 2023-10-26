#!/bin/bash

goose --version
ls -l /migrations
goose -dir /migrations postgres "$DB_STRING" up
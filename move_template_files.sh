#!/bin/sh

rsync -avh nomad-example-plugin-app/ .
rm -rfv nomad-example-plugin-app

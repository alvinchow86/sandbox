#!/bin/sh
PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=sandbox.settings py.test sandbox

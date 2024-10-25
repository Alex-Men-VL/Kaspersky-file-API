#!/bin/sh

set -o errexit
set -o nounset

readonly cmd="$*"

python ./manage.py migrate --noinput
python ./manage.py collectstatic --noinput

# Evaluating passed command (do not touch):
# shellcheck disable=SC2086
exec $cmd

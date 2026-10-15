#!/usr/bin/env bash
# Build the site in a Ruby 3.1 container (matches CI), without a local Ruby.
# Pulls the official image from the AWS ECR Public mirror of Docker Hub.
# Gems are cached in the "dcc-bundle" Docker volume.
#
# Usage: scripts/build-docker.sh [extra jekyll build args]
set -euo pipefail
cd "$(dirname "$0")/.."
docker run --rm \
  -v "$PWD":/srv -w /srv \
  -v dcc-bundle:/usr/local/bundle \
  -e JEKYLL_ENV=production \
  public.ecr.aws/docker/library/ruby:3.1 \
  bash -c 'bundle install --quiet && bundle exec jekyll build --baseurl /DynamicCareerCanvas "$@"' _ "$@"

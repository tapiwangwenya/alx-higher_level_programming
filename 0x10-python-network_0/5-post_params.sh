#!/bin/bash
# Bash scripts that sends a POST request to a given URL.
curl -s -X POST -d "email=test@gmail.com&subject=I always do my PROJECTS" "$1"

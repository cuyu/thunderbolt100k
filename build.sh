#!/usr/bin/env bash
sudo rm -rf dist
sudo python setup.py sdist bdist_wheel
twine upload dist/*
#!/usr/bin/env bash

# Cleanup backups on MacOS
for d in $(tmutil listlocalsnapshotdates); do sudo tmutil deletelocalsnapshots $d; done

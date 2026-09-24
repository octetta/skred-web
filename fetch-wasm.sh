#!/bin/bash
set -e
VERSION=$(cat WASM_VERSION.txt)
echo "Fetching version v${VERSION}..."
curl -L -o wasm.zip "https://github.com/octetta/pulp/releases/download/v${VERSION}/skred-${VERSION}-maxed-wasm.zip"
unzip -o wasm.zip "skred-${VERSION}-maxed/*"
mv skred-${VERSION}-maxed/skred_api.* .
rm -rf skred-${VERSION}-maxed wasm.zip
echo "Done."

#!/bin/bash
set -e
VERSION=$(cat WASM_VERSION.txt)
echo "Fetching version v${VERSION}..."
curl -L -O "https://github.com/octetta/pulp/releases/download/v${VERSION}/skred_api.js"
curl -L -O "https://github.com/octetta/pulp/releases/download/v${VERSION}/skred_api.wasm"
echo "Done."

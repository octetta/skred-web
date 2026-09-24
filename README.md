# Skred Web UI

This repository hosts the web-based user interface for [Skred](https://github.com/octetta/pulp), a powerful music programming and synthesis language.

## Live Demo

Try the interactive environment in your browser:  
👉 **[https://octetta.github.io/skred-web/](https://octetta.github.io/skred-web/)**

### Additional Tools & Pages

- **[Learn Skred](https://octetta.github.io/skred-web/learn.html)**: Interactive tutorial notebook to learn Skred.
- **[Tokyo ADC Stage](https://octetta.github.io/skred-web/tokyo-adc-stage.html)**: Presentation slides and live demos.
- **[Help / Reference](https://octetta.github.io/skred-web/help.html)**: Quick command reference.

## Local Development

If you want to run the web interface locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/octetta/skred-web.git
   cd skred-web
   ```

2. **Fetch the required WASM files:**
   The WebAssembly backend is pulled dynamically to keep this repository clean. Run the fetch script to download the pinned version from GitHub Releases:
   ```bash
   ./fetch-wasm.sh
   ```

3. **Start the local server:**
   Start a local Python HTTP server that correctly handles the Cross-Origin Isolation headers required for WASM multithreading:
   ```bash
   ./serve-wasm.sh
   ```

4. Open `http://localhost:8080` in your web browser.

## Deployment

This repository uses GitHub Actions to automatically fetch the pinned `skred_api.wasm` and deploy it along with the static HTML files to GitHub Pages. To update the version of the WASM backend used by the web UI, edit `WASM_VERSION.txt` and push to the `main` branch.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

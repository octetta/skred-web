# Skred Web UI

This repository hosts the web-based user interface for [Skred](https://github.com/octetta/pulp), a powerful music programming and synthesis language.

## Live Demo

Try the interactive environment in your browser:  
👉 **[https://octetta.github.io/skred-web/](https://octetta.github.io/skred-web/)**

### Additional Tools & Pages

- **[Learn Skred](https://octetta.github.io/skred-web/learn.html)**: Interactive tutorial notebook to learn Skred.
- **[Tokyo ADC Stage](https://octetta.github.io/skred-web/tokyo-adc-stage.html)**: Presentation slides and live demos.
- **[Minimal WASM Example](https://octetta.github.io/skred-web/help.html)**: Boilerplate integration example for web developers.
- **[Code BEAM Presentation](https://octetta.github.io/skred-web/codebeam.html)**: Slide deck mapping Pulp's architecture to the BEAM philosophy.

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

### Real-Time Presentation Editing

If you are editing presentations (like `codebeam.html` or `tokyo-adc-stage.html`) and want a real-time hot-reloading preview as you type, you can use `live-server` via `npx` (which bypasses the need for the Python server for pure UI edits):

```bash
npx live-server .
```
This will automatically open your default browser. Any changes you save in your text editor will instantly refresh the browser page, making it much easier to tweak slide layouts and fix wording.

## Deployment

This repository uses GitHub Actions to automatically fetch the pinned `skred_api.wasm` and deploy it along with the static HTML files to GitHub Pages. To update the version of the WASM backend used by the web UI, edit `WASM_VERSION.txt` and push to the `main` branch.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

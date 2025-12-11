# Minimal Python Playwright Dev Container Template

A minimal dev container setup for Python Playwright automation with Chrome browser. This template provides a ready-to-use development environment with no unnecessary overhead.

## Features

- 🐳 Minimal Docker dev container configuration
- 🎭 Playwright with Chrome browser support
- 🐍 Python 3.11
- 📝 Example scripts demonstrating common Playwright patterns

## Quick Start

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Getting Started

1. **Clone this repository**
   ```bash
   git clone <repository-url>
   cd template_minimal_python_playwright
   ```

2. **Open in VS Code**
   ```bash
   code .
   ```

3. **Reopen in Container**
   - Press `F1` or `Ctrl+Shift+P` (Windows/Linux) / `Cmd+Shift+P` (Mac)
   - Type "Dev Containers: Reopen in Container"
   - Wait for the container to build (first time takes a few minutes)

4. **Run the examples**
   ```bash
   python examples/01_hello_world.py
   python examples/02_form_filling.py
   python examples/03_reading_data.py
   python examples/04_clicking_buttons.py
   ```

## Examples Included

### 01_hello_world.py
Basic Playwright usage demonstrating:
- Launching a browser
- Navigating to a page
- Extracting text content
- Taking screenshots

### 02_form_filling.py
Form interaction demonstrating:
- Filling text fields
- Interacting with form elements
- Working with different input types

### 03_reading_data.py
Data extraction demonstrating:
- Reading text from elements
- Extracting attributes
- Querying multiple elements
- Structured data extraction

### 04_clicking_buttons.py
Dynamic interaction demonstrating:
- Clicking buttons and links
- Waiting for navigation
- Handling page transitions
- Going back/forward in browser history

## Project Structure

```
.
├── .devcontainer/
│   ├── devcontainer.json    # Dev container configuration
│   └── Dockerfile            # Container image definition
├── examples/
│   ├── 01_hello_world.py
│   ├── 02_form_filling.py
│   ├── 03_reading_data.py
│   └── 04_clicking_buttons.py
├── requirements.txt          # Python dependencies
├── .gitignore
└── README.md
```

## Customization

### Adding Dependencies

Add Python packages to `requirements.txt`:
```txt
playwright==1.40.0
requests==2.31.0
beautifulsoup4==4.12.2
```

Then rebuild the container or run:
```bash
pip install -r requirements.txt
```

### Running in Headed Mode

By default, browsers run in headless mode. To see the browser UI, modify the script:

```python
# Change this:
browser = p.chromium.launch(headless=True)

# To this:
browser = p.chromium.launch(headless=False)
```

Note: Headed mode requires X11 forwarding or similar display setup in containers.

## Tips

- All examples use `headless=True` for compatibility with containerized environments
- Screenshots are saved in the current working directory
- Use `page.wait_for_load_state("networkidle")` to ensure pages are fully loaded
- The dev container includes all necessary Chrome dependencies

## Troubleshooting

### Container build fails
- Ensure Docker is running
- Try rebuilding: `Dev Containers: Rebuild Container`

### Playwright browser not found
- The postCreateCommand should install Chrome automatically
- Manually run: `playwright install chrome`

### Permission errors
- The container runs as user `vscode` by default
- Ensure files are accessible within the container

## License

This is a template repository - use it as you wish!

## Contributing

Feel free to submit issues and pull requests to improve this template.
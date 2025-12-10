# agentic-ai
A repo for experimenting with Agentic AI and course work from Udacity's Agentic AI Nanodegree

## Setup

### Prerequisites

This project requires Python 3.10 or higher. The project uses **pyenv** to manage Python versions (recommended for macOS) and **venv** for project-specific environments.

#### Installing pyenv (macOS - Recommended)

1. Install pyenv using Homebrew:
```bash
brew install pyenv
```

2. Add pyenv to your shell configuration. For zsh (default on macOS):
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

3. Reload your shell configuration:
```bash
source ~/.zshrc
```

4. Install Python 3.11 (as specified in `.python-version`):
```bash
pyenv install 3.11
```

5. Verify pyenv is working:
```bash
pyenv version
```

When you `cd` into this project directory, pyenv will automatically use Python 3.11 (via the `.python-version` file).

**Note**: If you prefer not to use pyenv, you can use `python3` instead of `python` in the commands below. However, pyenv provides cleaner Python version management across projects.

### Installation

1. Verify Python version (should be 3.11 when in this directory):
```bash
python --version
# or if pyenv isn't set up yet:
python3 --version
```

2. Create and activate a virtual environment:
```bash
python -m venv agentic
# or if python command isn't available:
python3 -m venv agentic

source agentic/bin/activate  # On macOS/Linux
# or
agentic\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   
   Create a `.env` file in the project root with your API keys:
   ```bash
   # Create .env file
   cat > .env << EOF
   # OpenAI/Vocareum API Configuration
   VOCAREUM_API_KEY=your_vocareum_api_key_here
   
   # Optional: OpenAI API endpoint (uncomment if using OpenAI directly)
   # OPENAI_API_KEY=your_openai_api_key_here
   EOF
   ```
   
   Replace `your_vocareum_api_key_here` with your actual API key. The `.env` file is gitignored and will not be committed.

### Running Jupyter Notebooks

1. Make sure the virtual environment is activated (see above)

2. Start Jupyter:
```bash
jupyter notebook
```

3. Open the notebooks from the `1 - Prompting for Effective LLM Reasoning and Planning/` directory

## Troubleshooting

### "python: command not found" on macOS

On macOS, the `python` command is often not available by default. Solutions:

1. **Use pyenv (Recommended)**: Follow the pyenv installation steps above. Once configured, `python` will be available when you're in this project directory.

2. **Use python3 directly**: Replace `python` with `python3` in all commands:
   ```bash
   python3 -m venv agentic
   python3 --version
   ```

3. **Create an alias**: Add to `~/.zshrc`:
   ```bash
   alias python=python3
   ```

### pyenv not switching Python versions automatically

If pyenv doesn't automatically use the version from `.python-version`:

1. Verify pyenv is initialized in your shell:
   ```bash
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   source ~/.zshrc
   ```

2. Check if the Python version is installed:
   ```bash
   pyenv versions
   ```

3. If 3.11 isn't listed, install it:
   ```bash
   pyenv install 3.11
   ```

### Virtual environment issues

If you encounter issues with the virtual environment:

1. Delete and recreate it:
   ```bash
   rm -rf agentic
   python -m venv agentic
   source agentic/bin/activate
   pip install -r requirements.txt
   ```

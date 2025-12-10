# agentic-ai
A repo for experimenting with Agentic AI and course work from Udacity's Agentic AI Nanidegree

## Setup

### Prerequisites

This project requires Python 3.10 or higher. Check your Python version:
```bash
python --version
```

### Installation

1. Create and activate a virtual environment:
```bash
python -m venv agentic
source agentic/bin/activate  # On macOS/Linux
# or
agentic\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   
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

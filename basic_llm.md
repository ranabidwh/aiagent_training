

# Basic Local LLM Setup with Ollama

This guide will help you quickly set up and run a large language model (LLM) locally on your machine using Ollama. Ollama simplifies the process of getting LLMs like Mistral up and running.

---

## What is Ollama?

Ollama is a tool that allows you to run open-source large language models locally. It packages model weights, configurations, and data into a single, redistributable bundle, and provides a simple API and command-line interface for interaction.

## Prerequisites

* **Python 3.x:** Ensure you have Python installed. If not, please refer to our [Python Installation and Setup Guide](link_to_your_python_readme_section_here) for detailed instructions.
* **Internet Connection:** Required to download the Ollama application and the LLM model weights the first time.

---

## Setup Steps

Follow these steps to get your local LLM up and running:

### Step 1: Install Ollama
First, you need to install the Ollama application on your system. This is **not** a Python package but a standalone application that manages and runs the models.

**Option A: Download and Install (Recommended)**
The easiest way to install Ollama is to download the official application for your operating system:
1.  Go to the official Ollama website: [https://ollama.com/download](https://ollama.com/download)
2.  Download the installer for your operating system (macOS, Linux, Windows).
3.  Run the installer and follow the on-screen instructions.

**Option B: Using Pip (for Python integration and CLI access, but still needs the core Ollama app)**
While Ollama is a standalone app, you can install the `ollama` Python package to interact with it programmatically and get CLI tools. **Note: This package requires the core Ollama application to be installed first from the link above.**

```bash
pip install ollama
```

## Downloading Mistral
```bash
ollama run mistral
```

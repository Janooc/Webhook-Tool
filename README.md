# Webhook Tool

## Overview

The Webhook Tool is a Python-based utility designed to manage Discord webhooks. It provides functionalities to either spam a Discord webhook with custom messages or delete a webhook entirely using just its link. This tool is simple yet powerful, making it easy to test or disable webhooks.

## Features

- **Webhook Spammer:** Send multiple requests to a specified Discord webhook with customizable options such as message content, delay between requests, and threading for faster execution.
- **Webhook Deleter:** Permanently delete a Discord webhook using its link, ensuring it is no longer accessible.

## Installation

To get started with the Webhook Tool, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/webhook-tool.git
    cd webhook-tool
    ```

2. **Install Dependencies:**
    The tool requires a few Python packages. Install them using the following command:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Tool:**
    Execute the Python script to start the Webhook Tool:
    ```bash
    python webhook_tool.py
    ```

## Usage

Once the tool is running, you will be presented with a menu:

1. **Webhook Spammer:** Follow the prompts to input the webhook URL, message content, number of requests, delay, and whether you want to use threading.
2. **Webhook Deleter:** Simply provide the webhook URL you wish to delete.

## Requirements

- Python 3.x
- `requests`
- `aiohttp`
- `colorama`
- `pystyle`

All required Python packages are listed in the `requirements.txt` file.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to submit a pull request or open an issue.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to everyone who has contributed to improving this tool.

---

**Note:** This tool is intended for educational and testing purposes only. Misuse of this tool is not encouraged and should be avoided.

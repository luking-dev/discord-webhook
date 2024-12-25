# Discord Webhook

This project is an implementation of a webhook for Discord. It allows sending automated messages to a Discord channel using the Discord webhook API.

## Features

- Send messages to a specific Discord channel.
- Support for embedded messages.
- Easy configuration and use.

## Requirements

- Python
- Docker
- A Discord webhook URL

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/luking-dev/discord-webhook.git
    ```
2. Navigate to the project directory:
    ```bash
    cd discord-webhook
    ```
3. Build the Docker image:
    ```bash
    docker build -t discord-webhook .
    ```

## Usage

1. Configure the webhook URL in the `config.json` file:
    ```json
    {
      "webhookUrl": "https://discord.com/api/webhooks/your-webhook-id/your-webhook-token"
    }
    ```
2. Run the Docker container to send a message:
    ```bash
    docker run --rm discord-webhook "Your message here"
    ```

## Contributions

Contributions are welcome. Please open an issue or a pull request to discuss any changes you would like to make.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more details.
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

1. Configure the webhook URL creating an `.env` file:
    ```env
    DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/your-webhook-id/your-webhook-token"
    ```

> Note: To obtain the webhook URL for a specific Discord channel, follow these steps:
> 1. Open Discord and navigate to the server where you want to create the webhook.
> 2. Click on the server name at the top of the channel list to open the server settings.
> 3. In the server settings, click on "Integrations" in the left sidebar.
> 4. Under "Integrations," click on "Webhooks."
> 5. Click the "New Webhook" button.
> 6. Give your webhook a name and select the channel you want the webhook to post to.
> 7. Click the "Copy Webhook URL" button to copy the webhook URL to your clipboard.
> 8. Save the webhook URL for use in your application.

2. Run the Docker container to send a message:
    ```bash
    docker run --rm discord-webhook "Your message here"
    ```

## Contributions

Contributions are welcome. Please open an issue or a pull request to discuss any changes you would like to make.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more details.
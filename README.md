# Zhan: Love Message Image Generator Bot

Zhan is a Telegram bot that generates love message images. The bot overlays love phrases on randomly selected backgrounds with decorative elements and sends the resulting image back to the user. This project uses the Python Telegram Bot API (`telebot`) and the Python Imaging Library (`PIL`).

## Features

- Start command: Welcomes the user.
- Text message handler: Generates and sends an image with a love message.
- Randomly selects backgrounds, fonts, and decorative elements for image creation.

## Project Structure

```plaintext
├── bot.py
├── pic_overlaper.py
├── images
│   ├── backgrounds
│   ├── corner_elements
│   ├── vignettes
├── fonts
├── README.md
```

## Project Structure

- `bot.py`: Contains the main logic for the Telegram bot.
- `pic_overlapper.py`: Handles the image generation logic.
- `images/`: Contains subdirectories for backgrounds, corner elements, and vignettes used in the image creation.
- `fonts/`: Contains font files for text rendering on the images.

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/zhan.git
    cd zhan
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Prepare the environment variables**:
    Create a `.env` file in the project root directory and add your Telegram bot token:
    ```plaintext
    TELEGRAM_TOKEN=your-telegram-bot-token
    ```

4. **Organize the resources**:
    - Place background images in the `images/backgrounds` directory.
    - Place corner element images in the `images/corner_elements` directory.
    - Place vignette images in the `images/vignettes` directory.
    - Place font files in the `fonts` directory.

## Usage

1. **Run the bot**:
    ```bash
    python bot.py
    ```

2. **Interact with the bot on Telegram**:
    - Start the bot by sending `/start`.
    - Send any text message to receive an image with your love message.

## Functions

### bot.py

- **`handle_start(message)`**: Handles the `/start` command and sends a welcome message.
- **`handle_text(message)`**: Handles text messages, generates an image with the love message, and sends it back to the user.

### pic_overlapper.py

- **`get_elements_for_picture()`**: Selects random background, font, and decorative elements.
- **`paste_corner_elements(card_image, corner_elements)`**: Pastes corner elements onto the card image.
- **`draw_text_on_image(card_image, love_phrase, font_path, color)`**: Draws the love phrase text on the card image.
- **`draw_vignette(card_image, vignette_path)`**: Draws the vignette on the card image.
- **`love_func(love_phrase)`**: Combines all elements to generate the final love message image and returns it as a byte stream.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to improve the project.

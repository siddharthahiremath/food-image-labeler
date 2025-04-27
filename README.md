# Food Image Labeling and Reminder System

This project provides functionality to:
1. Take pictures using a webcam
2. Label food items in images using OpenAI's GPT-4 Vision API
3. Send email reminders using Gmail API

## Setup

1. Install required dependencies:
```bash
pip install opencv-python openai google-auth-oauthlib google-auth-httplib2 google-api-python-client python-dotenv
```

2. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key and Gmail configuration
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

3. Set up API credentials:
   - OpenAI API key (in .env file)
   - Google OAuth credentials (credentials.json)

## Usage

### Taking Pictures
```python
from t import take_picture
take_picture("output.jpg")
```

### Labeling Images
```python
from t import label_image
label = label_image("food_image.jpg")
print(label)
```

### Setting Reminders
```python
from t import set_reminder
set_reminder("your_email@example.com", "Reminder message", "10:00")
```

## Security Note
- Keep your API keys and credentials secure
- Never commit sensitive files like `token.json`, `credentials.json`, or `.env`
- Use environment variables for API keys in production
- The `.env.example` file shows what environment variables are needed

## License
MIT 
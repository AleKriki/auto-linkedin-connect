# Project Architecture

## Overview
This project is an automation bot designed to connect with recruiters on LinkedIn.  
It uses Selenium to control the browser and simulate user actions such as login, search, and sending connection requests.

## Folder Structure

src/
├── main.py # Entry point
├── config.py # Configurations (credentials, delays, etc.)
├── linkedin_bot.py # Main bot class
├── utils/ # Helper modules
│ ├── browser.py # Browser handling (Selenium)
│ ├── parser.py # Parsing extracted data
│ └── logger.py # Logging system
└── services/
└── linkedin_service.py # LinkedIn-specific automation functions

## Flow
1. Start bot (`main.py`)
2. Login into LinkedIn (`linkedin_bot.py`)
3. Search recruiters by keyword
4. Send connection requests automatically

## Technologies
- Python 3.12
- Selenium
- Chrome WebDriver

## Notes
⚠️ This project is for educational purposes only.  
Automating LinkedIn may violate its Terms of Service.

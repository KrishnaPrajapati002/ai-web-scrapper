AI Web Scraper with CAPTCHA Handling

This project is a Streamlit-based web scraping application that can extract website content and is designed to work with CAPTCHA-protected sites using a separate solver environment. The system is built in a modular way, where the scraper and CAPTCHA solver run in isolated virtual environments and communicate through a tool-calling pipeline.

Features

Streamlit web interface

Selenium-based dynamic website scraping

Separate CAPTCHA solver environment

Automatic integration between scraper and solver

Designed for structured data and metadata extraction

Extendable for legal document analysis and RAG systems

Project Structure
.
├── main.py               # Streamlit UI
├── scrape.py             # Web scraping logic
├── captcha_solver.py     # CAPTCHA solver (separate environment)
├── run_sbase.bat         # Run Streamlit app
├── run_captcha.bat       # Run CAPTCHA solver
├── .gitignore
└── README.md

Architecture
Streamlit UI
     |
     v
Scraper (Selenium)
     |
     v
CAPTCHA Solver (separate venv)
     |
     v
HTML / Metadata Output


Two virtual environments are used:

.env → Streamlit + Selenium (main application)

venv_captcha → CAPTCHA solver tools

Setup
1. Create Virtual Environments
python -m venv .env
python -m venv venv_captcha

2. Install Dependencies

For main app:

.env\Scripts\activate
pip install streamlit selenium


For CAPTCHA solver:

venv_captcha\Scripts\activate
pip install selenium selenium-recaptcha-solver

Running the Application

Start the main system:

run_sbase.bat


This will launch the Streamlit interface at:

http://localhost:8501

Purpose

This project is intended for:

Automated web data extraction

Legal judgment metadata processing

Research in information retrieval

AI agent pipelines (LangGraph / RAG)

Structured JSON generation from web sources

Legal Note

This project does not bypass security systems.
It supports official APIs, human-assisted CAPTCHA solving, and research-compliant automation.

Author

Krishna Prajapati
Computer Science (AI/ML)
Focus: Web Automation, Legal NLP, RAG, Intelligent Agents

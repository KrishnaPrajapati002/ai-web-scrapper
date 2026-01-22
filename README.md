AI Web Scraper with CAPTCHA Handling

This project is an AI-powered web scraping system built with Streamlit and Selenium that provides a user-friendly interface for extracting data from dynamic websites and is designed with a modular, agent-style architecture to handle CAPTCHA-protected pages using a separate solver environment, where the main application runs in one virtual environment for the UI and scraping logic and a second isolated environment runs the CAPTCHA handling tool, with both parts connected through a subprocess-based pipeline; the system is intended for structured metadata extraction, legal and research-oriented web data collection, and future integration with RAG and intelligent agent frameworks, follows clean separation of concerns, avoids direct security bypass, and is suitable for extending into large-scale document analysis and semantic search workflows.

Krishna Prajapati
Computer Science (AI/ML)
Focus: Web Automation, Legal NLP, RAG, Intelligent Agents

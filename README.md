# Job Application Automation

This repository contains a Python-based solution to automate the job application process using Selenium WebDriver and the OpenAI API. The automation script logs into LinkedIn, searches for specific job titles based on a YAML configuration file, extracts job descriptions, and generates customized cover letters. It then attaches the resume and cover letter (if required) and submits the job application automatically.

## Features

- Automates LinkedIn job searches based on job titles and locations.
- Extracts job descriptions and uses ChatGPT to generate tailored cover letters.
- Automatically attaches resumes and cover letters and submits job applications.
- Configurable through a YAML file.

## Technologies

- Python
- Selenium WebDriver
- OpenAI GPT API
- YAML

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/imsirmayor/job-application-automation.git
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your job search details to `config.yaml`.

4. Run the main script:
   ```bash
   python main.py
   ```

## Configuration

Edit the `config.yaml` file to specify:

- Job titles and countries for the search
- LinkedIn credentials
- OpenAI API key
- Resume details


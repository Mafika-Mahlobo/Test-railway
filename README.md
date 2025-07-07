# Survey web application

This is a web-based survey portal built using Flask, HTML, CSS, jQuery, and Python.

## Table of Contents
- [Introduction](#Introduction)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#Usage)

## Introduction
This project was built as part of an assessment to prove basic programming principles. Visit live demo here: [here]().

## Dependencies
- Flask: Web framework for Python
- jQuery: JavaScript library for simplifying HTML DOM traversal and manipulation
- MYSQL Server
- python-dotenv
- Other Python Dependencies as listed in requirements.txt

## T run locally

1. You need to have python3 installed on your machine.

2. Download and install MYSQL (*follow the prompt to create a user account*).

3. Create a .env file in the root folder and save your MYSQL details as shown below.

```bash
DB_USER=Database_user
DB_PASSWORD=Database_Password
DB_HOST=Database_host
DB_NAME=Dnatabase_name
```

4. Create Database (*you might need to run the command inside the MYSQL folder*).

```bash
mysql -u {your usernme} -p < createDB.sql
```

5. Clone the repository to your local machine:
```bash
git clone https://github.com/Mafika-Mahlobo/tshimologong-project
```

6. Cd to the project folder
```bash
cd Simple_Survey
```

7. Install more dependencies using the following command or install them manually. (*you might need to run the following command in you C drive*)

```bash
pip install -r requirements.txt
```

## Usage

- Start the Flask server:

```bash
python3 python3 app.py
```
- Open your web browser and navigate to http://127.0.0.1:5000 to access the Survey web application.

-Start with gunicorn server:

```bash
python3 gunicorn app:app
```
*note: may not be compatable with windows system*
- Open your web browser and navigate to http://127.0.0.1:8000 to access the Survey web application.

# Survey web application

This is a dynamic web-based survey application built with Flask, Python, HTML, CSS, and jQuery. The platform allows users to submit survey responses and view live aggregated results in real-time.

This project was developed as part of a software development internship application at  [Tshimologong Digital Innovation Precinct](https://tshimologong.joburg/).

[Visti the live demo](https://simple-survey-production.up.railway.app/)

## What to install it locally?

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#Usage)

## Dependencies

- Flask: Web framework for Python
- jQuery: JavaScript library for simplifying HTML DOM traversal and manipulation
- MYSQL Server
- python-dotenv
- Other Python Dependencies as listed in requirements.txt

## Installation

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
git clone https://github.com/Mafika-Mahlobo/Simple-Survey
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
 *Open your web browser and navigate to http://127.0.0.1:5000 to access the Survey web application.*

- Start with gunicorn server:

```bash
python3 gunicorn app:app
```
*Open your web browser and navigate to http://127.0.0.1:8000 to access the Survey web application.*

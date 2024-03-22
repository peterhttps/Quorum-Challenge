# Quorum Challenge 🏛️

Welcome to the repository for the Quorum Challenge, a project developed to meet the specific needs of Quorum's hiring process. This document provides instructions on how to get the project running on your local machine, either directly or via Docker, as well as an overview of its functionalities.

## 🛠 Setup & Installation

Whether you prefer a Dockerized environment or a more traditional Python setup, we've got you covered. Follow these steps to get started:

### 🐍 Running Locally (Without Docker)

1. **Clone and set up a virtual environment:**
```bash
$ git clone https://github.com/peterhttps/Quorum-Challenge
$ cd Quorum-Challenge
$ python -m venv .venv
$ .\.venv\Scripts\activate # On Windows
$ source .venv/bin/activate # On Linux/Mac
```
2. **Install dependencies:**
```bash
$ pip install -r requirements.txt
```
3. **Environment Variables:**
- Copy `.env.dist` to `.env` and configure it based on your local setup.
4. **Run the server:**
```bash
$ uvicorn app:asgi_app --reload 
```

### 🐳 Running with Docker
1. **Environment Variables**
- Copy `.env.dist` to `.env` and configure it based on your local setup.
2. **Build and Run the Docker container:**
```bash
$ make up -d
```
Visit `http://localhost:9001` in your browser to see the application in action.

## 🔍 Overview of Functionalities

The application features some endpoints that provide access to legislative data, processed and served in a user-friendly format. Below is a brief overview:

- `/bill`: Retrieves a list of bills with detailed information.
- `/legislator`: Displays data on legislators, including their participation in bills.

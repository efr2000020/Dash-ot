# Dash-ot - IoT Dashboard

## Overview

Dash-ot is a simple web-based IoT dashboard built with Django. It allows users to register, manage, and delete IoT devices (nodes) with sensors and actuators.

## Features

- Add/Remove Nodes

## Prerequisites

Ensure you have the following installed:

- Python (>=3.8)
- pip
- Virtual environment tool (venv)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Dash-ot.git
cd Dash-ot
```

### 2. Create and Activate a Virtual Environment

#### On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Now, open your browser and visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- **Add a Node:** Click "Add Node" to register a new IoT device.
- **View Nodes:** Navigate to "Node List" to see all registered devices.
- **Delete a Node:** Click "Delete" to remove a node from the system.


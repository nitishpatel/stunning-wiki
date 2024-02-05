# Wiki Most Common Count Application

## Overview

This is a FastAPI application that utilizes the Wikipedia API to fetch search results and count the most common words in the summary.

## Prerequisites

- Python 3.11 or later
- Pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nitishpatel/stunning-wiki.git
   ```

2. Change into the project directory:

   ```bash
   cd stunning-wiki
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

   Replace `main` with the name of the Python file containing your FastAPI app instance.

2. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the root endpoint.

## API Endpoints

### 1. Root Endpoint

- **URL:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Method:** GET
- **Description:** Welcome message.

### 2. Wikipedia Count Endpoint

- **URL:** [http://127.0.0.1:8000/wikipedia-count/](http://127.0.0.1:8000/wikipedia-count/)
- **Method:** POST
- **Request Payload:** JSON with `title` (string) and `count` (integer) fields.
- **Description:** Fetch Wikipedia search results and count the most common words in the summary.

### 3. Search Results Endpoint

- **URL:** [http://127.0.0.1:8000/search-results/](http://127.0.0.1:8000/search-results/)
- **Method:** GET
- **Description:** Retrieve search results stored in the in-memory database.

## Example Usage

- Open the provided [FastAPI Swagger documentation](http://127.0.0.1:8000/docs) for detailed information and testing the API endpoints.
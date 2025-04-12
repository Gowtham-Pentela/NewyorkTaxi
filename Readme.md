# New York Taxi Data Pipeline

---

## Overview
This project implements a data pipeline for processing New York Taxi trip data. The pipeline automates the process of downloading raw data, transforming it, and loading it into a SQLite database for further analysis. The pipeline is integrated with Jenkins for Continuous Integration (CI) and Continuous Deployment (CD), ensuring automated testing and deployment.

---

## Features
- **Data Ingestion**: Downloads raw taxi trip data from a public URL.
- **Data Transformation**: Cleans and processes the raw data to prepare it for analysis.
- **Data Loading**: Loads the transformed data into a SQLite database.
- **Automated Testing**: Ensures code quality and correctness using `pytest`.
- **CI/CD Integration**: Automates the pipeline using Jenkins for continuous integration and deployment.

---

## Project Structure
- `NewyorkTaxi/`
  - `data/` - Directory for storing raw and processed data
  - `pipeline/` - Core pipeline scripts
    - `__init__.py` - Marks the directory as a Python package
    - `extract.py` - Handles data downloading
    - `transform.py` - Handles data transformation
    - `load.py` - Handles loading data into SQLite
    - `main.py` - Orchestrates the pipeline
  - `tests/` - Unit tests for the pipeline
    - `test_transform.py` - Tests for the transform module
  - `requirements.txt` - Python dependencies
  - `Jenkinsfile` - Jenkins pipeline definition
  - `.gitignore` - Files and directories to ignore in Git
  - `README.md` - Project documentation

## Technologies Used
- **Python**: Core programming language for the pipeline.
- **Pandas**: For data manipulation and transformation.
- **PySpark**: For distributed data processing.
- **SQLite**: Lightweight database for storing transformed data.
- **Jenkins**: CI/CD tool for automating the pipeline.
- **pytest**: For unit testing.

---

## Pipeline Workflow
The pipeline is defined in the `Jenkinsfile` and consists of the following stages:

1. **Checkout**:
   - Pulls the latest code from the GitHub repository.

2. **Set Up Virtual Environment**:
   - Creates a Python virtual environment.
   - Installs dependencies from `requirements.txt`.

3. **Prepare Data Directory**:
   - Ensures the `data/` directory exists to store raw and processed data.

4. **Download Data**:
   - Downloads the raw taxi trip data from a public URL using Python's `requests` library.

5. **Run Tests**:
   - Executes unit tests using `pytest` to validate the code.

6. **Run Pipeline**:
   - Executes the main pipeline script (`pipeline/main.py`) to process the data.

7. **Post Actions**:
   - Logs success or failure messages based on the pipeline's outcome.

---

## How to Run the Project

### 1. Prerequisites
- Python 3.8 or higher
- Jenkins installed and configured
- Git installed
- SQLite installed (optional, for local database access)

### 2. Clone the Repository
```bash
git clone https://github.com/Gowtham-Pentela/NewyorkTaxi.git
cd NewyorkTaxi 
```
### 3. Set Up the Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
pip install --upgrade pip
pip install -r [requirements.txt]
```
### 4. Run the Pipeline Locally
```bash
python [main.py]
```
### 5. Run Tests
```bash 
pytest tests/
```
### 6. Run the Pipeline in Jenkins

1. Configure Jenkins to use the `Jenkinsfile` in the repository.  
2. Trigger the pipeline from the Jenkins dashboard.

---

## 🛠️ Jenkins Pipeline

The `Jenkinsfile` defines the CI/CD pipeline with the following stages:

- **Checkout**: Pulls the latest code from GitHub.  
- **Set Up Virtual Environment**: Installs dependencies in a virtual environment.  
- **Prepare Data Directory**: Ensures the `data/` directory exists.  
- **Download Data**: Downloads the raw data file.  
- **Run Tests**: Executes unit tests using `pytest`.  
- **Run Pipeline**: Runs the main pipeline script.

---

## 📈 Improvements

- **Add More Tests**  
  - Include integration tests and performance tests.

- **Static Code Analysis**  
  - Use tools like `pylint` or `flake8` to enforce coding standards.

- **Code Coverage**  
  - Measure test coverage using `pytest-cov`.

- **Dockerize the Application**  
  - Use Docker to containerize the pipeline for consistent environments.

- **Deploy to Cloud**  
  - Deploy the pipeline to cloud platforms like AWS, Azure, or GCP.

- **Notifications**  
  - Configure Jenkins to send notifications via email or Slack.

---

## 🤝 Contributing

1. Fork the repository.  
2. Create a new branch. 
``` bash
git checkout -b feature-branch
``` 
3. Commit your changes. 
``` bash
git commit -m "Add new feature"
``` 
4. Push to the branch.  
``` bash
git push origin feature-branch
```
5. Open a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



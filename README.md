# SPE Scientific Calculator with DevOps

A command-line scientific calculator implemented in Python and integrated with a CI/CD pipeline using DevOps tools.

This project demonstrates how a simple Python application can be automatically tested, containerized, built, and deployed using Jenkins, Docker, DockerHub, and Ansible.

---

# Features

The calculator supports the following mathematical operations:

- Addition  
- Subtraction  
- Multiplication  
- Division  
- Factorial  
- Natural Logarithm (ln)  
- Power function  
- Square root  

The application runs through a menu-driven command line interface (CLI).

---

# Project Structure

```
scientific-calculator
│
├── calculator
│   ├── __init__.py
│   ├── main.py
│   └── operations.py
│
├── tests
│   └── test_calculator.py
│
├── ansible
│   ├── deploy.yml
│   └── inventory.ini
│
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── README.md
└── .gitignore
```

### Folder Description

| Component | Purpose |
|---|---|
| `calculator/` | Main calculator application code |
| `operations.py` | Mathematical function implementations |
| `main.py` | CLI interface for user interaction |
| `tests/` | Unit tests using Pytest |
| `ansible/` | Automated deployment scripts |
| `Dockerfile` | Container build instructions |
| `Jenkinsfile` | CI/CD pipeline definition |

---

# Running the Calculator Locally

From the project root directory:

```
python3 calculator/main.py
```

This launches the menu-driven calculator interface.

Example menu:

```
Scientific Calculator
1. add
2. subtract
3. multiply
4. divide
5. factorial
6. ln
7. power
8. sqrt
9. exit
```

---

# Running Unit Tests

The project includes automated unit tests for all operations.

Run tests using:

```
pytest -v
```

Example output:

```
tests/test_calculator.py::test_add PASSED
tests/test_calculator.py::test_subtract PASSED
tests/test_calculator.py::test_multiply PASSED
tests/test_calculator.py::test_divide PASSED
tests/test_calculator.py::test_factorial PASSED
tests/test_calculator.py::test_ln PASSED
tests/test_calculator.py::test_power PASSED
tests/test_calculator.py::test_sqrt PASSED
```

---

# Docker Containerization

The application is containerized using Docker to ensure consistent execution across environments.

### Build Docker Image

```
docker build -t key717/scientific-calculator .
```

### Run Container

```
docker run -d --name scientific-calculator key717/scientific-calculator:latest
```

### Verify Running Container

```
docker ps
```

Example output:

```
CONTAINER ID   IMAGE                                 STATUS
xxxxxxx        key717/scientific-calculator:latest   Up
```

The Docker image is published on DockerHub:

```
https://hub.docker.com/r/key717/scientific-calculator
```

---

# CI/CD Pipeline

The project implements a complete CI/CD pipeline using Jenkins.

Pipeline stages include:

1. Clone Repository  
2. Install Dependencies  
3. Run Tests  
4. Build Docker Image  
5. Push Docker Image to DockerHub  
6. Deploy using Ansible  

---

# Automated Deployment with Ansible

Deployment is automated using an Ansible playbook.

The playbook performs the following tasks:

1. Stops any existing container
2. Removes the previous container
3. Pulls the latest Docker image from DockerHub
4. Starts a new container using the updated image

Run the deployment manually using:

```
ansible-playbook -i ansible/inventory.ini ansible/deploy.yml
```

Example Ansible output:

```
TASK [Stop old container]
TASK [Remove old container]
TASK [Pull latest Docker image]
TASK [Run calculator container]

PLAY RECAP
localhost : ok=5 changed=4 failed=0
```

---

# CI/CD Workflow

The complete workflow of the system is:

```
Developer
   ↓
GitHub Repository
   ↓
Jenkins Pipeline
   ↓
Automated Testing (Pytest)
   ↓
Docker Image Build
   ↓
DockerHub Registry
   ↓
Ansible Deployment
   ↓
Running Docker Container
```

---

# Technologies Used

- Python – Application implementation  
- Pytest – Automated testing  
- Git & GitHub – Version control  
- Jenkins – Continuous Integration pipeline  
- Docker – Application containerization  
- DockerHub – Image registry  
- Ansible – Automated deployment  

---

# Project Goal

The goal of this project is to demonstrate how DevOps practices can automate software delivery using a CI/CD pipeline.

The pipeline ensures that every code update is automatically:

- Tested  
- Built  
- Containerized  
- Pushed to a registry  
- Deployed  

This improves software reliability, reproducibility, and deployment efficiency.

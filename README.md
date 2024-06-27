# AIToolsBox

Welcome to **AIToolsBox**! This project is a comprehensive example of building and deploying AI-powered microservices using FastAPI. It demonstrates clean architecture, dependency injection, and advanced microservices practices. The project currently includes an OCR service leveraging Tesseract OCR, and will be expanded to include additional AI services in the future. Additionally, AIToolsBox comes with a React-based web application and a Flutter-based Android client.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Clean Architecture](#clean-architecture)
- [Prerequisites](#prerequisites)
- [Setup and Deployment](#setup-and-deployment)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

**AIToolsBox** is designed to be a learning resource and a practical example of implementing AI-powered microservices with a focus on clean architecture. It features:

- A microservice architecture using FastAPI.
- A Tesseract OCR service for extracting text from images.
- Centralized logging and monitoring using the EFK stack (Elasticsearch, Fluent Bit, Kibana).
- API management and routing through Traefik.
- HTTP & gRPC communication between services.

## Features

- **Microservices with FastAPI**: Each service is implemented using FastAPI with clean architecture principles and dependency injection for maintainability and scalability.
- **Tesseract OCR Service**: Utilizes Tesseract OCR to extract text from images.
- **Traefik API Gateway**: Manages routing and load balancing, accessible via `http://localhost:8080`.
- **EFK Stack for Logging**: Centralized logging using Elasticsearch, Fluent Bit, and Kibana, accessible via `http://localhost:5601`.

[//]: # (- **Web Application**: React-based web interface for user interaction.)
[//]: # (- **Mobile Application**: Flutter-based Android client for accessing AI tools on the go.)
- **Simplified Deployment**: Easy setup and deployment scripts for both Windows and Linux users.

## Clean Architecture

AIToolsBox follows the principles of Clean Architecture in each service to ensure that services are:

- **Independent of frameworks**: The core application logic is not dependent on any specific framework or external technology.
- **Testable**: Each component is isolated and can be tested independently.
- **Independent of UI**: The user interface can change without altering the business logic.
- **Independent of Database**: The database can be swapped without changing the business logic.

## Prerequisites

To run this project, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.10+](https://www.python.org/downloads/)

## Setup and Deployment

### Cloning the Repository

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/your-username/AIToolsBox.git
cd AIToolsBox
```

### Running the Services
#### Windows
To run the services on Windows, execute the following command:

```bash
cd deployment
deply.bat
```

#### Linux
To run the services on Linux, execute the following command:

```bash
cd deployment
./deploy.sh
```

These scripts will build and start all microservices, the Traefik API gateway, and the EFK stack.

### Accessing the Services

- **IAM Service**: 'http://iam.localhost'
- **Media Service**: 'http://media.localhost'
- **OCR Service**: 'http://ocr.localhost'
- **Traefik Dashboard**: 'http://localhost:8080'
- **Kibana Dashboard**: 'http://localhost:5601'


## Usage

- **IAM Service**: Handles user registration, authentication and authorization.
- **Media Service**: Manages operations related to media files.
- **OCR Service**: Extracts text from images using Tesseract OCR.
- **Traefik Dashboard**: Provides an overview of the services and routing configuration.
- **Kibana Dashboard**: Displays logs and metrics for monitoring.


## Contributing
Contributions are welcome! To contribute, follow these steps:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.
7. Sit back and relax while your PR is reviewed.


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact
If you have any questions or suggestions, feel free to reach out to me at:
- Email: esaminu.py@gmail.com
- LinkedIn: [linkedin.com/aminupy](www.linkedin.com/in/mohamadamin-eskandari-28377b225)
- GitHub: [github.com/aminupy](https://github.com/aminupy)

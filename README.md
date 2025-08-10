# DevOps Capstone Project

![Build Status](https://github.com/HossamJa/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://shields.io/)

## Overview

This repository contains the completed DevOps Capstone Project for the IBM DevOps and Software Engineering Professional Certificate. The project demonstrates hands-on application of DevOps principles, including Agile planning, Test-Driven Development (TDD), Continuous Integration (CI), security enhancements, containerization, Kubernetes deployment, and automated Continuous Delivery (CD) pipelines.

In this capstone, I developed a secure microservices-based Customer Accounts application using Flask. The application manages customer data (create, read, update, delete, and list operations) and is deployed on a cloud-native environment. Over several sprints, I built an Agile plan, implemented the RESTful API, ensured high code coverage, automated CI/CD pipelines, and deployed to Kubernetes/OpenShift.

Key accomplishments:
- Created an Agile plan with user stories and a Kanban board using GitHub and ZenHub.
- Developed the microservice using TDD, achieving 95%+ code coverage.
- Implemented CI with GitHub Actions for automated builds, tests, linting, and coverage checks.
- Added security features like HTTP security headers and CORS policies.
- Containerized the app with Docker and deployed manually to Kubernetes/OpenShift.
- Built an automated CD pipeline using Tekton for cloning, linting, testing, building, and deploying.
- Completed peer review and submitted all required evidence.

This project showcases my skills in full-stack DevOps, from planning to production deployment, making it ideal for demonstrating to employers.

## Table of Contents

- [Overview](#overview)
- [Project Goals](#project-goals)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Agile Planning (Sprint 0)](#agile-planning-sprint-0)
- [Sprint 1: RESTful Service Development with TDD](#sprint-1-restful-service-development-with-tdd)
- [Sprint 2: Continuous Integration and Security](#sprint-2-continuous-integration-and-security)
- [Sprint 3: Containerization, Deployment, and CD Pipeline](#sprint-3-containerization-deployment-and-cd-pipeline)
- [Evidence and Screenshots](#evidence-and-screenshots)
- [License](#license)

## Project Goals

The goal was to build a Customer Accounts microservice that:
- Handles CRUD+L (Create, Read, Update, Delete, List) operations for customer data.
- Uses a PostgreSQL database.
- Follows Agile methodologies for planning and execution.
- Employs TDD for robust, tested code.
- Integrates CI/CD for automation.
- Ensures security and cloud-native deployment.

The project was completed over multiple sprints, simulating a real-world DevOps team environment.

## Technologies Used

- **Programming Language**: Python 3.9
- **Web Framework**: Flask
- **Database**: PostgreSQL
- **Testing**: Nose (nosetests), Coverage.py (95%+ coverage)
- **Linting**: Flake8
- **Security**: Flask-Talisman (security headers), Flask-CORS (CORS policies)
- **CI/CD**: GitHub Actions (CI), Tekton (CD pipeline)
- **Containerization**: Docker
- **Orchestration**: Kubernetes/OpenShift
- **Project Management**: GitHub (Repo, Kanban, Issues), ZenHub
- **Other Tools**: Gunicorn (WSGI server), Buildah (image building), OpenShift Client

## Project Structure

The code follows the Model-View-Controller (MVC) pattern:

```
├── service         <- Microservice package
│   ├── common/     <- Common log and error handlers
│   ├── config.py   <- Flask configuration object
│   ├── models.py   <- Database models and business logic
│   └── routes.py   <- REST API routes
├── tests           <- Unit and integration tests
│   ├── factories.py            <- Test factories
│   ├── test_cli_commands.py    <- CLI tests
│   ├── test_models.py          <- Model unit tests
│   └── test_routes.py          <- Route unit tests
├── tekton          <- Tekton pipeline definitions
│   ├── pipeline.yaml
│   └── tasks.yaml
├── .github/workflows/ci-build.yaml  <- GitHub Actions CI workflow
├── Dockerfile      <- Docker image definition
├── deployment.yaml <- Kubernetes manifests
├── setup.cfg       <- Tools setup config
├── requirements.txt<- Python dependencies
├── pipelinerun.txt <- Tekton pipeline run logs
├── README.md       <- This file
└── screenshots/    <- Evidence screenshots (all .PNG format)
```

Data Model (Account):
| Field        | Type       | Optional |
|--------------|------------|----------|
| id           | Integer    | False    |
| name         | String(64) | False    |
| email        | String(64) | False    |
| address      | String(256)| False    |
| phone_number | String(32) | True     |
| date_joined  | Date       | False    |

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/HossamJa/devops-capstone-project.git
   cd devops-capstone-project
   ```

2. Set up the environment (source the setup script):
   ```
   source bin/setup.sh
   ```

3. Install dependencies:
   ```
   make install
   ```

4. Start PostgreSQL (via Docker):
   ```
   make db
   ```

5. Run the application locally:
   ```
   flask run
   ```

For Kubernetes/OpenShift deployment, see [Sprint 3](#sprint-3-containerization-deployment-and-cd-pipeline).

## Usage

- **Local Development**: Run `flask run` and access at `http://127.0.0.1:5000/accounts`.
- **API Endpoints**:
  - POST `/accounts`: Create an account.
  - GET `/accounts`: List all accounts.
  - GET `/accounts/<id>`: Read an account.
  - PUT `/accounts/<id>`: Update an account.
  - DELETE `/accounts/<id>`: Delete an account.

Example CURL commands (from Sprint 1 demo):
- Create: `curl -i -X POST http://127.0.0.1:5000/accounts -H "Content-Type: application/json" -d '{"name":"John Doe","email":"john@doe.com","address":"123 Main St.","phone_number":"555-1212"}'`
- List: `curl -i -X GET http://127.0.0.1:5000/accounts`
- Read: `curl -i -X GET http://127.0.0.1:5000/accounts/1`
- Update: `curl -i -X PUT http://127.0.0.1:5000/accounts/1 -H "Content-Type: application/json" -d '{"name":"John Doe","email":"john@doe.com","address":"123 Main St.","phone_number":"555-1111"}'`
- Delete: `curl -i -X DELETE http://127.0.0.1:5000/accounts/1`

Run tests: `nosetests` (ensure 95% coverage with `coverage report`).

## Agile Planning (Sprint 0)

I started with Agile planning in GitHub, creating a repository, Kanban board, user story template, and product backlog. User stories were prioritized, labeled, and estimated with story points. This formed the basis for all sprints.

- Created GitHub repo and Kanban board.
- Developed user story template (`user-story.md`).
- Added and sorted user stories for building the microservice.
- Refined backlog and built sprint plans.

**Planning Repository**
![Planning Repository](screenshots/planning-repository-done.PNG)

**User Story Template**
![User Story Template](screenshots/planning-storytemplate-done.PNG)

**User Stories on Kanban**
![User Stories on Kanban](screenshots/planning-userstories-done.PNG)

**Product Backlog**
![Product Backlog](screenshots/planning-productbacklog-done.PNG)

**Labels**
![Labels](screenshots/planning-labels-done.PNG)

**Kanban Board**
![Kanban Board](screenshots/planning-kanban-done.PNG)


## Sprint 1: RESTful Service Development with TDD

Configured the environment, cloned the repo, and developed the microservice using TDD. Implemented READ, UPDATE, DELETE, and LIST endpoints. Achieved 95% code coverage with nosetests and coverage tool. Demonstrated functionality in a sprint review using CURL.

- Workflow: Branch per story, write failing tests, implement code, maintain coverage, PR to main.
- Moved stories through Kanban: Backlog → In Progress → Done → Closed.

**Setup.cfg**
![Setup.cfg](screenshots/rest-setupcfg-done.PNG)

**Tech Debt on Kanban**
![Tech Debt on Kanban](screenshots/rest-techdebt-done.PNG)

**List Accounts Done**
![List Accounts Done](screenshots/list-accounts.PNG)

**Read Accounts Done**
![Read Accounts Done](screenshots/read-accounts.PNG)

**Update Accounts Done**
![Update Accounts Done](screenshots/update-accounts.PNG)

**Delete Accounts Done**
![Delete Accounts Done](screenshots/delete-accounts.PNG)

**Create Demo**
![Create Demo](screenshots/rest-create-done.PNG)

**List Demo**
![List Demo](screenshots/rest-list-done.PNG)

**Read Demo**
![Read Demo](screenshots/rest-read-done.PNG)

**Update Demo**
![Update Demo](screenshots/rest-update-done.PNG)

**Delete Demo** 
![Delete Demo](screenshots/rest-delete-done.PNG)

## Sprint 2: Continuous Integration and Security

Planned Sprint 2, added CI with GitHub Actions (triggered on push/PR, includes build, test, lint, coverage). Added security: Flask-Talisman for headers, Flask-CORS for policies. Wrote TDD tests for security features.

- CI Workflow: Builds/tests on events, uses Flake8 and nosetests.
- Security: Added headers and CORS, verified with tests.

**Sprint 2 Plan**
![Sprint 2 Plan](screenshots/sprint2-plan.PNG)

**CI Workflow Run** 
![CI Workflow Run](screenshots/ci-workflow-done.PNG)

**CI Badge in README**
![CI Badge in README](screenshots/ci-badge-done.PNG)

**CI Kanban Done**
![CI Kanban Done](screenshots/ci-kanban-done.PNG)

**Security Code** 
![Security Code](screenshots/security-code-done.PNG)

**Security Headers Output**
![Security Headers Output](screenshots/security-headers-done.PNG)

**Security Kanban Done**
![Security Kanban Done](screenshots/security-kanban-done.PNG)

## Sprint 3: Containerization, Deployment, and CD Pipeline

Planned Sprint 3, containerized with Docker, manually deployed to OpenShift/Kubernetes, then automated CD with Tekton pipeline (clone, lint, test, build, deploy).

- Dockerfile: Based on Python 3.9-slim, installs deps, uses Gunicorn, non-root.
- Manual Deploy: Created PostgreSQL service, manifests, deployed image.
- CD Pipeline: Tekton tasks for flake8, nosetests, buildah, openshift-client.

**Sprint 3 Plan**
![Sprint 3 Plan](screenshots/sprint3-plan.PNG)

**App Output in Browse**
![App Output in Browser](screenshots/kube-app-output.PNG)

**Docker Done on Kanban**
![Docker Done on Kanban](screenshots/kube-docker-done.PNG)

**Docker Images** 
![Docker Images](screenshots/kube-images.PNG)

**Kubernetes Deployment**
![Kubernetes Deployment](screenshots/kube-deploy-accounts.PNG)

**Kubernetes Done on Kanban**
![Kubernetes Done on Kanban](screenshots/kube-kubernetes-done.PNG)

**CD Pipeline Done**
![CD Pipeline Done](screenshots/cd-pipeline-done.PNG)

**Pipeline logs available in** [pipelinerun.txt](pipelinerun.txt).

## Evidence and Screenshots

All evidence screenshots are in the `/screenshots` folder. URLs:
- GitHub Repo: https://github.com/HossamJa/devops-capstone-project
- Dockerfile: https://github.com/HossamJa/devops-capstone-project/blob/main/Dockerfile

The project was submitted for peer review, including all screenshots and URLs as per the rubric.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

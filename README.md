# 🤖 ML CI/CD Pipeline — AZ-400 DevOps Portfolio

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Hub](https://img.shields.io/badge/Docker%20Hub-Image%20Registry-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Status](https://img.shields.io/badge/Pipeline-Passing-brightgreen?style=for-the-badge)

> A production-style ML model deployment pipeline demonstrating core DevOps engineering
> practices — built entirely on GitHub with no external cloud dependencies.

---

## 📋 Table of Contents

- [Purpose](#purpose)
- [Why GitHub Native](#why-github-native)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Pipeline Stages](#pipeline-stages)
- [Technologies](#technologies)
- [ML Model](#ml-model)
- [Run Locally](#run-locally)
- [Lessons Learned](#lessons-learned)
- [Credits](#credits)

---

## 💼 Purpose

This project was built as part of a deliberate transition from **Data Science to DevOps Engineering**, using the AZ-400 DevOps Engineer Expert certification as a framework.

The goal was not just to train an ML model — but to build the **infrastructure around it** that makes it deployable, testable, and maintainable in a real-world production environment.

Specifically, this project demonstrates:

| Concept | Implementation |
|---|---|
| **CI/CD Pipelines** | GitHub Actions workflow with 2 automated stages |
| **Pipeline as Code** | Entire pipeline defined in `ci-cd.yml` |
| **Automated Testing** | pytest blocks deployment if any test fails |
| **Containerization** | Dockerfile packages app + model together |
| **Image Registry** | Docker Hub stores versioned container images |
| **Environment Parity** | Same container runs in all environments |
| **Release Gates** | Build stage only runs if all tests pass |

---

## 🐙 Why GitHub Native

This pipeline was built entirely within the GitHub ecosystem — using **GitHub Actions** for CI/CD and **Docker Hub** for image storage — rather than relying on Azure DevOps or other external platforms.

**The reasons for this are deliberate:**

**Accessibility** — GitHub Actions requires zero infrastructure setup. Any developer can fork this repo and have the pipeline running in minutes with no cloud account required.

**Industry adoption** — GitHub Actions is one of the most widely used CI/CD platforms in the industry today, making this a highly transferable skill across companies and teams.

**Simplicity** — By keeping everything on GitHub, the pipeline is easier to understand, audit, and maintain. There are no external service connections, no Azure subscriptions, and no billing surprises.

**Portfolio visibility** — Recruiters and hiring managers can see the pipeline running live directly on the GitHub repo — no need to log into a separate platform to verify the work.

**Docker Hub** was chosen as the image registry because it is the most widely recognised container registry in the industry, is free for public images, and integrates seamlessly with GitHub Actions.

---

## 🏗️ Architecture
```
GitHub Push
     │
     ▼
GitHub Actions
     │
     ├──▶ Job 1: Run Tests
     │         │
     │         ├── Install dependencies
     │         ├── Train ML model
     │         └── Run pytest (6 tests)
     │                  │
     │              ✅ Pass → continue
     │              ❌ Fail → pipeline stops
     │
     └──▶ Job 2: Build & Push Docker Image
               │
               ├── Build Docker image
               └── Push to Docker Hub
                        │
                   lindiwe22/iris-model-api:latest
```

---

## 📁 Project Structure
```
ML-CI-CD-Pipeline/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions pipeline definition
├── app/
│   └── main.py                # FastAPI app serving predictions
├── model/
│   └── train.py               # Trains and saves the ML model
├── tests/
│   └── test_app.py            # Automated tests (6 test cases)
├── Dockerfile                 # Containerizes the app + model
├── requirements.txt           # Python dependencies
└── README.md
```

---

## 🚀 Pipeline Stages

### Job 1 — Run Tests (CI)
Triggered automatically on every push to `main` and on every pull request.

- Sets up Python 3.11 on a fresh Ubuntu runner
- Installs all dependencies from `requirements.txt`
- Trains the ML model to generate the `.pkl` file needed for tests
- Runs `pytest` across 6 test cases covering all API endpoints
- **Blocks the build stage if any test fails** — this is the gate that protects production

### Job 2 — Build & Push Docker Image (CD)
Only runs if Job 1 passes, and only on pushes to `main` (not pull requests).

- Logs into Docker Hub using GitHub repository secrets
- Builds the Docker image from the `Dockerfile`
- Pushes two tags to Docker Hub:
  - `latest` — always points to the most recent build
  - `run_number` — immutable tag for traceability and rollback

---

## 🛠️ Technologies

**Languages & Environment**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-000000?style=for-the-badge&logo=yaml&logoColor=white)

**Machine Learning**

![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

**API & Serving**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)

**Containerization & Registry**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Hub](https://img.shields.io/badge/Docker%20Hub-2496ED?style=for-the-badge&logo=docker&logoColor=white)

**CI/CD**

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

**Testing**

![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![HTTPX](https://img.shields.io/badge/HTTPX-009688?style=for-the-badge&logo=python&logoColor=white)

| Category | Tools |
|---|---|
| **Languages** | Python 3.11, YAML |
| **Machine Learning** | Scikit-learn, NumPy |
| **API & Serving** | FastAPI, Uvicorn, Pydantic |
| **Containerization** | Docker, Docker Hub |
| **CI/CD** | GitHub Actions |
| **Testing** | Pytest, HTTPX |

---

## 🤖 ML Model

- **Dataset:** Iris — a classic multiclass classification dataset
- **Algorithm:** Random Forest Classifier (scikit-learn)
- **Accuracy:** ~97% on test set
- **Output:** Predicted species + confidence score

### Sample API Request
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }'
```

### Sample Response
```json
{
  "species": "setosa",
  "confidence": 0.97,
  "model_version": "1.0.0"
}
```

---

## ⚙️ Run Locally
```bash
# Clone the repo
git clone https://github.com/AZ400-DevOps-Portfolio/ML-CI-CD-Pipeline.git
cd ML-CI-CD-Pipeline

# Install dependencies
pip install -r requirements.txt

# Train the model
python model/train.py

# Start the API
uvicorn app.main:app --reload

# Run tests
pytest tests/ -v
```

### With Docker
```bash
# Pull from Docker Hub
docker pull lindiwe22/iris-model-api:latest

# Or build locally
docker build -t iris-model-api .

# Run the container
docker run -p 8000:8000 iris-model-api
```

---

## 🪨 Lessons Learned

Building this pipeline was not without its challenges. These are real stumbling blocks encountered along the way — documented here because debugging is a core DevOps skill.

**1. Hidden folder creation in github.dev**
Creating the `.github/workflows/` folder structure in the browser-based editor was tricky. Typing the full path as a filename (e.g. `.github/workflows/ci-cd.yml`) caused the entire path to become the filename rather than creating nested folders. The fix was to create each folder explicitly using right-click → New Folder before creating the file inside it.

**2. Incorrect folder names on push**
The `tests/` folder was initially pushed as `test/` and the `Dockerfile` was pushed as `Docker` — both caused pipeline failures. GitHub Actions is case-sensitive and path-exact, so the pipeline could not find the files it expected.

**3. Syntax errors from pasting code**
Pasting code into github.dev sometimes introduced invisible formatting characters and curly quotes that caused Python `SyntaxError` failures in the pipeline runner. The fix was to clear the file completely and re-paste clean plain text.

**4. Docker Hub secrets not persisting across repos**
When the repository was deleted and recreated, the GitHub Actions secrets (`DOCKER_USERNAME` and `DOCKER_PASSWORD`) were lost with it. Secrets are scoped to a specific repository and must be re-added after recreation.

**5. Azure subscription friction**
The original plan was to connect this pipeline to Azure DevOps and deploy to Azure Web Apps. However, Azure's free trial required credit card verification which created a barrier. This led to the decision to build everything GitHub-native — which ultimately resulted in a cleaner, more accessible, and more portable pipeline.

---

## 🙏 Credits

**Developed by Lindiwe Songelwa — Data Scientist | DevOps Engineer | Insight Creator**

| Platform | Link |
|---|---|
| 💼 LinkedIn | [Lindiwe S.](https://www.linkedin.com/in/lindiwe-songelwa) |
| 🌐 Portfolio | [Creative Portfolio](https://lindiwe-22.github.io/Portfolio-Website/) |
| 🏅 Credly | [Lindiwe Songelwa – Badges](https://www.credly.com/users/samnkelisiwe-lindiwe-songelwa) |
| 🐳 Docker Hub | [lindiwe22/iris-model-api](https://hub.docker.com/r/lindiwe22/iris-model-api) |
| 📧 Email | [sl.songelwa@hotmail.co.za](mailto:sl.songelwa@hotmail.co.za) |

---

*© 2026 Lindiwe Songelwa. All rights reserved.*
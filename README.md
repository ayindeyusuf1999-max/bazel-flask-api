# Bazel Flask API

A Python Flask REST API built and tested using **Bazel** as the build system, with a fully automated **GitHub Actions CI pipeline**.

## Live Demo
https://bazel-flask-api.onrender.com

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome message |
| `/health` | GET | Health check |
| `/info` | GET | App info |

## Tech Stack
- Python + Flask
- Bazel (build system)
- GitHub Actions (CI/CD)
- Render (deployment)

## Project Structure
## How to Run Locally
```bash
pip install flask
python app/main.py
```

## How to Build with Bazel
```bash
bazel build //app:server
```

## How to Test
```bash
pytest tests/test_main.py -v
```

## CI Pipeline
Every push to `main` triggers GitHub Actions to:
1. Install Bazel
2. Build the app with Bazel
3. Run tests with pytest
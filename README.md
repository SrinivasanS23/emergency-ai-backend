# Emergency AI – Disaster Message Classification System

## Overview
Emergency AI is a backend system that analyzes text messages to identify emergency situations, classify the type of disaster, and assign a severity score using NLP techniques.

## Features
- Emergency vs Non-emergency detection
- Disaster category classification (Fire, Flood, Medical, etc.)
- Rule-based severity scoring
- REST API built with Django & Django REST Framework

## Tech Stack
- Python
- Django, Django REST Framework
- Scikit-learn (NLP)
- SQLite
- AWS EC2 (deployment)

## API Endpoint
POST /api/analyze/

Request:
{
  "message": "Fire broke out near bus stand"
}

Response:
{
  "is_emergency": true,
  "category": "fire",
  "severity": 2
}

## Deployment
The application is deployed on AWS EC2 and can be started/stopped to manage costs.


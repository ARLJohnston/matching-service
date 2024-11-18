# Matching Service for UofG SPA

This server, built using FastAPI, is dedicated to processing allocation data and returning results using a specialized matching algorithm. It is designed exclusively to support the `spa` project. A web platform for handling Student Project Allocation.


## Tech Stack
- Python: The core language used for building the server and the matching algorithms.
- FastAPI: A modern, fast (high-performance), web framework for building APIs.
- Pydantic: Used for data validation and type annotations.
- [matchingproblems](https://github.com/fmcooper/matchingproblems): The library that implements all the matching algorithms used by the service.

## Building

To build the docker image, run

    docker build -t matching-service:latest .

## Running

To run the docker image, run

    docker run -p 8000:8000 matching-service

To run the server locally, run:

    uv run fastapi dev


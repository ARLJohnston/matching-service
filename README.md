# Matching Service for allocation-app

This server, built using FastAPI, is dedicated to processing allocation data and returning results using a specialised matching algorithm. It is designed to support the `uofg-socs-amps/spa` project. A web platform for handling Student Project Allocation.


## Tech Stack
- Python
- FastAPI
- Pydantic
- [matchingproblems](https://github.com/fmcooper/matchingproblems)

## Building

To build the docker image, run

    docker build -t matching-service:latest .

## Running

To run the docker image, run

    docker run -p 8000:8000 matching-service



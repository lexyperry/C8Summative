# Inventory System

## How to Run
> `python3 -m venv venv`
> `source venv/bin/activate`
> `pip install -r requirements.txt`
Run Flask API: > `python app.py`
Run CLI: > `python cli.py`

## API Endpoints
- GET `/inventory`
- POST `/inventory`
- PATCH `/inventory/<id>`
- DELETE `/inventory/<id>`

## Features
- Lookup food details on OpenFoodFacts
- CLI interface

## Test Data
- Run the database: > python app.py
- Run the CLI: > python cli.py
- Test Product = {
    Name: Thai peanut noodle kit includes stir-fry rice noodles & thai peanut seasoning
    Stock: 10
    Price: 3.49
    Barcode: 737628064502
}
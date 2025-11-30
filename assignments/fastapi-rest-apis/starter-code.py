"""
FastAPI REST API Starter Code
Mergington High School - Computer Science

This starter code provides the basic structure for building a REST API with FastAPI.
Complete the TODO sections to implement the full CRUD functionality.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

# Create FastAPI application instance
app = FastAPI(
    title="Student API",
    description="A simple REST API for managing student records",
    version="1.0.0"
)

# TODO: Define your Pydantic models here
# Example:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None


# TODO: Create an in-memory data store
# Example: items = []


# TODO: Implement the root endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Student API"}


# TODO: Implement POST endpoint to create a new item
# @app.post("/items", status_code=status.HTTP_201_CREATED)
# def create_item(item: Item):
#     pass


# TODO: Implement GET endpoint to retrieve all items
# @app.get("/items")
# def get_all_items():
#     pass


# TODO: Implement GET endpoint to retrieve a single item by ID
# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     pass


# TODO: Implement PUT endpoint to update an item
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     pass


# TODO: Implement DELETE endpoint to remove an item
# @app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_item(item_id: int):
#     pass


# Run the application with: uvicorn starter-code:app --reload
# Access documentation at: http://localhost:8000/docs

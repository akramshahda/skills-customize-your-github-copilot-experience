# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern, fast REST APIs using the FastAPI framework in Python. You'll create endpoints, handle requests, manage data validation, and implement best practices for API development.

## 📝 Tasks

### 🛠️ Create Basic API Structure

#### Description
Set up a FastAPI application with basic configuration and create your first endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Install and import FastAPI and uvicorn
- Create a FastAPI application instance
- Implement a root endpoint (`/`) that returns a JSON welcome message
- Include proper HTTP status codes in responses
- Run the development server successfully

### 🛠️ Implement CRUD Operations

#### Description
Build a complete set of Create, Read, Update, and Delete endpoints for managing a resource (e.g., tasks, books, or students).

#### Requirements
Completed program should:

- Create a POST endpoint to add new items with request body validation
- Create a GET endpoint to retrieve all items
- Create a GET endpoint to retrieve a single item by ID
- Create a PUT endpoint to update an existing item
- Create a DELETE endpoint to remove an item
- Use Pydantic models for request and response validation
- Store data in a simple in-memory structure (list or dictionary)

### 🛠️ Add Error Handling and Documentation

#### Description
Enhance your API with proper error handling, status codes, and take advantage of FastAPI's automatic documentation features.

#### Requirements
Completed program should:

- Return appropriate HTTP status codes (200, 201, 404, 400, etc.)
- Implement error handling for invalid IDs or missing resources
- Add descriptive docstrings and response descriptions to endpoints
- Include query parameters for filtering or searching data
- Access and verify the auto-generated API documentation at `/docs`

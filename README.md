# Project Management API

This is a RESTful API built with FastAPI that implements user authentication using JWT (JSON Web Token) and Role-Based Access Control (RBAC). The API manages users with different roles and restricts access to certain endpoints based on the user’s role. It is designed to be deployed using AWS Lambda and API Gateway.

## Features

- **User Registration and Login**: Users can register with a username and password. Passwords are securely hashed using bcrypt. Users can log in and receive a JWT token upon successful authentication.
- **JWT-based Authorization**: The API uses JWT tokens for authenticating users. The token includes user information such as user ID and role and is validated in subsequent API requests.
- **Role-Based Access Control (RBAC)**: Implements at least two roles: admin and user. Admin users can access protected endpoints for creating, updating, or deleting resources, while user roles can only access read-only endpoints.
- **CRUD Operations for Resources**: Basic CRUD operations for a sample resource (e.g., “projects”) are implemented. Admin users can create, update, delete, and view resources, while user roles can only view resources.
- **MongoDB (MongoEngine)**: Uses MongoDB to store user information and resources. MongoEngine is used as the ODM (Object Data Mapper) for interacting with MongoDB.

## Tech Stack

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **MongoDB**: A NoSQL database used to store user and project data.
- **Motor**: An asynchronous driver for MongoDB.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Python-Jose**: A library to handle JWT encoding and decoding.
- **Passlib**: A password hashing library for Python.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/project-management-api.git
   cd project-management-api
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add the following:
   ```env
   MONGODB_URL=mongodb+srv://<username>:<password>@<cluster-url>/<dbname>?retryWrites=true&w=majority
   DATABASE_NAME=project_db
   SECRET_KEY=your-secret-key-for-jwt
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API documentation**:
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Deployment

To deploy the API on AWS Lambda using API Gateway, follow these steps:

1. **Package the application**: Use a tool like `Zappa` or `Serverless` to package and deploy your FastAPI application to AWS Lambda.
2. **Configure API Gateway**: Set up API Gateway to route requests to your Lambda function.
3. **Environment Variables**: Ensure that all necessary environment variables are set in the AWS Lambda environment.

## Example Endpoints

1. **User Registration**:
   - `POST /register`
   - Body: `{ "username": "example", "password": "password123", "role": "user" }`

2. **User Login**:
   - `POST /login`
   - Body: `{ "username": "example", "password": "password123" }`
   - Response: `{ "access_token": "JWT_TOKEN" }`

3. **Get Projects (for all users)**:
   - `GET /projects`
   - (Requires JWT)

4. **Create Project (admin only)**:
   - `POST /projects`
   - Body: `{ "name": "Project A", "description": "Description of project" }`
   - (Requires JWT with admin role)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 
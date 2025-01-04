from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import auth, projects

app = FastAPI(
    title="Project Management API",
    description="API with JWT Authentication and RBAC",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, tags=["Authentication"])
app.include_router(projects.router, tags=["Projects"])


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to the Project Management API",
        "docs": "/docs",
        "redoc": "/redoc",
    }

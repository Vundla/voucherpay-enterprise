from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth,
    users,
    jobs,
    finance,
    energy,
    carbon,
    ai,
    policy,
    accessibility,
    analytics
)

api_router = APIRouter()

# Authentication endpoints
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# Core module endpoints
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
api_router.include_router(finance.router, prefix="/finance", tags=["Finance"])
api_router.include_router(energy.router, prefix="/energy", tags=["Energy"])
api_router.include_router(carbon.router, prefix="/carbon", tags=["Carbon"])
api_router.include_router(ai.router, prefix="/ai", tags=["AI"])
api_router.include_router(policy.router, prefix="/policy", tags=["Policy"])

# Accessibility and empowerment endpoints
api_router.include_router(accessibility.router, prefix="/accessibility", tags=["Accessibility"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
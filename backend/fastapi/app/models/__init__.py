# Import all models to ensure they are registered with SQLAlchemy
from .user import User, UserProfile, AccessibilityProfile
from .job import (
    Job, JobApplication, JobCategory,
    FinanceRecord, BusinessFunding, Grant,
    EnergyUsage, EnergyProject, SustainabilityGoal,
    CarbonFootprint, CarbonOffset, CarbonProject,
    AIAssistance, AIRecommendation, AccessibilityAI,
    Policy, PolicyCompliance, AdvocacyCase,
    AnalyticsEvent, UserActivity, AccessibilityMetric
)
from .notification import Notification, EmailTemplate

# Base class for all models
from .user import Base

# Make all models available for import
__all__ = [
    "Base",
    "User",
    "UserProfile", 
    "AccessibilityProfile",
    "Job",
    "JobApplication",
    "JobCategory",
    "FinanceRecord",
    "BusinessFunding",
    "Grant",
    "EnergyUsage",
    "EnergyProject",
    "SustainabilityGoal",
    "CarbonFootprint",
    "CarbonOffset",
    "CarbonProject",
    "AIAssistance",
    "AIRecommendation",
    "AccessibilityAI",
    "Policy",
    "PolicyCompliance",
    "AdvocacyCase",
    "AnalyticsEvent",
    "UserActivity",
    "AccessibilityMetric",
    "Notification",
    "EmailTemplate"
]
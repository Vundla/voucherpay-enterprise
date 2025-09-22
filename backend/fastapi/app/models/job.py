# Placeholder model files for the other modules

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, JSON, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

# Job models
class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    accessibility_accommodations = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class JobApplication(Base):
    __tablename__ = "job_applications"
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    accommodation_requests = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class JobCategory(Base):
    __tablename__ = "job_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    accessibility_friendly = Column(Boolean, default=False)

# Finance models  
class FinanceRecord(Base):
    __tablename__ = "finance_records"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    type = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class BusinessFunding(Base):
    __tablename__ = "business_funding"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    disability_specific = Column(Boolean, default=False)
    amount_available = Column(Float)

class Grant(Base):
    __tablename__ = "grants"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    disability_focused = Column(Boolean, default=False)
    amount = Column(Float)

# Energy models
class EnergyUsage(Base):
    __tablename__ = "energy_usage"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    usage_kwh = Column(Float)
    date = Column(DateTime(timezone=True))

class EnergyProject(Base):
    __tablename__ = "energy_projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    accessibility_features = Column(JSON)

class SustainabilityGoal(Base):
    __tablename__ = "sustainability_goals"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    goal_type = Column(String(100))
    target_value = Column(Float)

# Carbon models
class CarbonFootprint(Base):
    __tablename__ = "carbon_footprints"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    co2_tons = Column(Float)
    date = Column(DateTime(timezone=True))

class CarbonOffset(Base):
    __tablename__ = "carbon_offsets"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    offset_tons = Column(Float)
    project_id = Column(Integer, ForeignKey("carbon_projects.id"))

class CarbonProject(Base):
    __tablename__ = "carbon_projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    inclusive_design = Column(Boolean, default=False)

# AI models
class AIAssistance(Base):
    __tablename__ = "ai_assistance"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    assistance_type = Column(String(100))
    request_data = Column(JSON)
    response_data = Column(JSON)

class AIRecommendation(Base):
    __tablename__ = "ai_recommendations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    recommendation_type = Column(String(100))
    content = Column(JSON)

class AccessibilityAI(Base):
    __tablename__ = "accessibility_ai"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    ai_feature = Column(String(100))
    settings = Column(JSON)

# Policy models
class Policy(Base):
    __tablename__ = "policies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    content = Column(Text)
    disability_related = Column(Boolean, default=False)

class PolicyCompliance(Base):
    __tablename__ = "policy_compliance"
    id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(Integer, ForeignKey("policies.id"))
    organization_id = Column(Integer)
    compliance_level = Column(String(50))

class AdvocacyCase(Base):
    __tablename__ = "advocacy_cases"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    case_type = Column(String(100))
    description = Column(Text)
    status = Column(String(50))

# Analytics models
class AnalyticsEvent(Base):
    __tablename__ = "analytics_events"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    event_type = Column(String(100))
    event_data = Column(JSON)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="analytics_events")

class UserActivity(Base):
    __tablename__ = "user_activities"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    activity_type = Column(String(100))
    duration_seconds = Column(Integer)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class AccessibilityMetric(Base):
    __tablename__ = "accessibility_metrics"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    metric_type = Column(String(100))
    value = Column(Float)
    date = Column(DateTime(timezone=True), server_default=func.now())
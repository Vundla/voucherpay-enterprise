from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, JSON, ForeignKey, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum
import uuid

Base = declarative_base()


class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    MODERATOR = "moderator"
    ADVOCATE = "advocate"
    EMPLOYER = "employer"


class DisabilityType(str, Enum):
    VISUAL = "visual"
    HEARING = "hearing"
    MOTOR = "motor"
    COGNITIVE = "cognitive"
    NEUROLOGICAL = "neurological"
    MULTIPLE = "multiple"
    OTHER = "other"
    PREFER_NOT_TO_SAY = "prefer_not_to_say"


class AccessibilityNeed(str, Enum):
    SCREEN_READER = "screen_reader"
    HIGH_CONTRAST = "high_contrast"
    LARGE_TEXT = "large_text"
    KEYBOARD_NAVIGATION = "keyboard_navigation"
    VOICE_CONTROL = "voice_control"
    MOTOR_ASSISTANCE = "motor_assistance"
    COGNITIVE_SUPPORT = "cognitive_support"
    CAPTIONS = "captions"
    SIGN_LANGUAGE = "sign_language"


class User(Base):
    """User model with comprehensive accessibility support"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(36), default=lambda: str(uuid.uuid4()), unique=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    
    # Personal Information
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone = Column(String(20))
    
    # Account Status
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    is_2fa_enabled = Column(Boolean, default=False)
    totp_secret = Column(String(32))
    
    # Role and Permissions
    role = Column(SQLEnum(UserRole), default=UserRole.USER)
    
    # Social Login
    google_id = Column(String(100), unique=True)
    github_id = Column(String(100), unique=True)
    linkedin_id = Column(String(100), unique=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login = Column(DateTime(timezone=True))
    
    # Relationships
    profile = relationship("UserProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    accessibility_profile = relationship("AccessibilityProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    analytics_events = relationship("AnalyticsEvent", back_populates="user", cascade="all, delete-orphan")


class UserProfile(Base):
    """Extended user profile information"""
    __tablename__ = "user_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    
    # Personal Details
    date_of_birth = Column(DateTime)
    gender = Column(String(20))
    location = Column(String(200))
    bio = Column(Text)
    profile_picture = Column(String(500))
    
    # Professional Information
    job_title = Column(String(100))
    company = Column(String(100))
    industry = Column(String(100))
    experience_years = Column(Integer)
    skills = Column(JSON)  # Array of skills
    education = Column(JSON)  # Array of education objects
    
    # Empowerment Preferences
    seeks_employment = Column(Boolean, default=False)
    seeks_housing = Column(Boolean, default=False)
    seeks_funding = Column(Boolean, default=False)
    seeks_support_services = Column(Boolean, default=False)
    
    # Privacy Settings
    profile_visibility = Column(String(20), default="public")  # public, private, contacts
    contact_preferences = Column(JSON)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="profile")


class AccessibilityProfile(Base):
    """Accessibility needs and preferences"""
    __tablename__ = "accessibility_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    
    # Disability Information (Optional)
    has_disability = Column(Boolean)
    disability_types = Column(JSON)  # Array of DisabilityType
    disability_description = Column(Text)
    
    # Accessibility Needs
    accessibility_needs = Column(JSON)  # Array of AccessibilityNeed
    assistive_technologies = Column(JSON)  # Array of assistive tech used
    
    # Accommodations
    workplace_accommodations = Column(JSON)
    communication_preferences = Column(JSON)
    mobility_requirements = Column(JSON)
    
    # Interface Preferences
    preferred_font_size = Column(Integer, default=16)
    high_contrast_mode = Column(Boolean, default=False)
    reduced_motion = Column(Boolean, default=False)
    screen_reader_user = Column(Boolean, default=False)
    keyboard_only_navigation = Column(Boolean, default=False)
    
    # Support Needs
    requires_support_person = Column(Boolean, default=False)
    support_person_contact = Column(String(255))
    emergency_contact = Column(JSON)
    
    # Privacy
    share_accessibility_info = Column(Boolean, default=False)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="accessibility_profile")
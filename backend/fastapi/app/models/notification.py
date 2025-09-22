from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, JSON, ForeignKey, Float, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum

Base = declarative_base()

class NotificationType(str, Enum):
    EMAIL = "email"
    PUSH = "push"
    SMS = "sms"
    IN_APP = "in_app"

class NotificationPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"

class Notification(Base):
    """Notification model with accessibility support"""
    __tablename__ = "notifications"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Content
    title = Column(String(200), nullable=False)
    message = Column(Text, nullable=False)
    type = Column(SQLEnum(NotificationType), default=NotificationType.IN_APP)
    priority = Column(SQLEnum(NotificationPriority), default=NotificationPriority.MEDIUM)
    
    # Accessibility
    screen_reader_text = Column(Text)  # Optimized text for screen readers
    high_contrast_version = Column(Text)  # High contrast version
    
    # Status
    is_read = Column(Boolean, default=False)
    is_sent = Column(Boolean, default=False)
    sent_at = Column(DateTime(timezone=True))
    
    # Metadata
    data = Column(JSON)  # Additional notification data
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="notifications")

class EmailTemplate(Base):
    """Email template model with accessibility features"""
    __tablename__ = "email_templates"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Template Info
    name = Column(String(100), nullable=False, unique=True)
    subject = Column(String(200), nullable=False)
    html_content = Column(Text, nullable=False)
    text_content = Column(Text, nullable=False)  # Plain text version for accessibility
    
    # Accessibility Features
    screen_reader_optimized = Column(Boolean, default=True)
    high_contrast_version = Column(Text)  # High contrast HTML version
    wcag_compliant = Column(Boolean, default=True)
    
    # Template Variables
    variables = Column(JSON)  # List of available template variables
    
    # Status
    is_active = Column(Boolean, default=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
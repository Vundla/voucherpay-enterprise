from pydantic_settings import BaseSettings
from typing import List, Optional
import os


class Settings(BaseSettings):
    """Application settings with accessibility and empowerment focus"""
    
    # Application
    APP_NAME: str = "VoucherPay Enterprise"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # Database
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "voucherpay_user"
    DB_PASSWORD: str = "password"
    DB_NAME: str = "voucherpay_enterprise"
    
    @property
    def DATABASE_URL(self) -> str:
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: Optional[str] = None
    
    @property
    def REDIS_URL(self) -> str:
        if self.REDIS_PASSWORD:
            return f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:4200", "http://localhost:3000"]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    
    def _parse_cors_origins(self, v):
        if isinstance(v, str):
            return [i.strip() for i in v.split(",")]
        return v
    
    # Email
    EMAIL_HOST: str = "smtp.gmail.com"
    EMAIL_PORT: int = 587
    EMAIL_USERNAME: str = ""
    EMAIL_PASSWORD: str = ""
    EMAIL_FROM: str = "noreply@voucherpay.com"
    EMAIL_USE_TLS: bool = True
    
    # OAuth
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    GITHUB_CLIENT_ID: str = ""
    GITHUB_CLIENT_SECRET: str = ""
    LINKEDIN_CLIENT_ID: str = ""
    LINKEDIN_CLIENT_SECRET: str = ""
    
    # File Upload
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    UPLOAD_DIR: str = "uploads"
    ALLOWED_FILE_TYPES: List[str] = ["jpg", "jpeg", "png", "pdf", "doc", "docx"]
    
    # Accessibility
    ACCESSIBILITY_AUDIT_ENABLED: bool = True
    ACCESSIBILITY_LOG_LEVEL: str = "INFO"
    WCAG_COMPLIANCE_LEVEL: str = "AA"
    
    # Analytics
    ANALYTICS_ENABLED: bool = True
    ANALYTICS_RETENTION_DAYS: int = 90
    REAL_TIME_ANALYTICS: bool = True
    
    # Security
    RATE_LIMIT_REQUESTS_PER_MINUTE: int = 100
    SECURITY_HEADERS_ENABLED: bool = True
    
    # 2FA
    TOTP_ISSUER: str = "VoucherPay Enterprise"
    TOTP_ALGORITHM: str = "SHA1"
    TOTP_DIGITS: int = 6
    TOTP_PERIOD: int = 30
    
    # Monitoring
    SENTRY_DSN: Optional[str] = None
    LOG_LEVEL: str = "INFO"
    METRICS_ENABLED: bool = True
    
    # Empowerment Features
    SOCIAL_SECURITY_MODULE_ENABLED: bool = True
    HOUSING_MODULE_ENABLED: bool = True
    BUSINESS_FUNDING_MODULE_ENABLED: bool = True
    NON_DISCRIMINATION_MODULE_ENABLED: bool = True
    AI_ASSISTANCE_MODULE_ENABLED: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Create settings instance
settings = Settings()
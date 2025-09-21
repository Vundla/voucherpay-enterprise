import dotenv from 'dotenv';

dotenv.config();

export const config = {
  // Server
  NODE_ENV: process.env.NODE_ENV || 'development',
  PORT: parseInt(process.env.PORT || '3000'),
  
  // Database
  DB_HOST: process.env.DB_HOST || 'localhost',
  DB_PORT: parseInt(process.env.DB_PORT || '3306'),
  DB_USERNAME: process.env.DB_USER || 'voucherpay_user',
  DB_PASSWORD: process.env.DB_PASSWORD || 'password',
  DB_NAME: process.env.DB_NAME || 'voucherpay_enterprise',
  
  // JWT
  JWT_SECRET: process.env.JWT_SECRET || 'your-secret-key',
  JWT_ACCESS_TOKEN_EXPIRE: process.env.JWT_ACCESS_TOKEN_EXPIRE_MINUTES || '30',
  JWT_REFRESH_TOKEN_EXPIRE: process.env.JWT_REFRESH_TOKEN_EXPIRE_DAYS || '7',
  
  // CORS
  CORS_ORIGINS: process.env.CORS_ORIGINS?.split(',') || ['http://localhost:4200', 'http://localhost:3000'],
  
  // Rate Limiting
  RATE_LIMIT_REQUESTS_PER_MINUTE: parseInt(process.env.RATE_LIMIT_REQUESTS_PER_MINUTE || '100'),
  
  // Email
  EMAIL_HOST: process.env.EMAIL_HOST || 'smtp.gmail.com',
  EMAIL_PORT: parseInt(process.env.EMAIL_PORT || '587'),
  EMAIL_USERNAME: process.env.EMAIL_USERNAME || '',
  EMAIL_PASSWORD: process.env.EMAIL_PASSWORD || '',
  EMAIL_FROM: process.env.EMAIL_FROM || 'noreply@voucherpay.com',
  
  // OAuth
  GOOGLE_CLIENT_ID: process.env.GOOGLE_CLIENT_ID || '',
  GOOGLE_CLIENT_SECRET: process.env.GOOGLE_CLIENT_SECRET || '',
  GITHUB_CLIENT_ID: process.env.GITHUB_CLIENT_ID || '',
  GITHUB_CLIENT_SECRET: process.env.GITHUB_CLIENT_SECRET || '',
  LINKEDIN_CLIENT_ID: process.env.LINKEDIN_CLIENT_ID || '',
  LINKEDIN_CLIENT_SECRET: process.env.LINKEDIN_CLIENT_SECRET || '',
  
  // Redis
  REDIS_HOST: process.env.REDIS_HOST || 'localhost',
  REDIS_PORT: parseInt(process.env.REDIS_PORT || '6379'),
  REDIS_PASSWORD: process.env.REDIS_PASSWORD || '',
  
  // File Upload
  MAX_FILE_SIZE: parseInt(process.env.MAX_FILE_SIZE || '10485760'), // 10MB
  UPLOAD_DIR: process.env.UPLOAD_DIR || 'uploads',
  
  // Accessibility
  ACCESSIBILITY_AUDIT_ENABLED: process.env.ACCESSIBILITY_AUDIT_ENABLED === 'true',
  WCAG_COMPLIANCE_LEVEL: process.env.WCAG_COMPLIANCE_LEVEL || 'AA',
  
  // Analytics
  ANALYTICS_ENABLED: process.env.ANALYTICS_ENABLED === 'true',
  REAL_TIME_ANALYTICS: process.env.REAL_TIME_ANALYTICS === 'true',
  
  // 2FA
  TOTP_ISSUER: process.env.TOTP_ISSUER || 'VoucherPay Enterprise',
  
  // Empowerment Features
  SOCIAL_SECURITY_MODULE_ENABLED: process.env.SOCIAL_SECURITY_MODULE_ENABLED !== 'false',
  HOUSING_MODULE_ENABLED: process.env.HOUSING_MODULE_ENABLED !== 'false',
  BUSINESS_FUNDING_MODULE_ENABLED: process.env.BUSINESS_FUNDING_MODULE_ENABLED !== 'false',
  NON_DISCRIMINATION_MODULE_ENABLED: process.env.NON_DISCRIMINATION_MODULE_ENABLED !== 'false',
  AI_ASSISTANCE_MODULE_ENABLED: process.env.AI_ASSISTANCE_MODULE_ENABLED !== 'false',
};
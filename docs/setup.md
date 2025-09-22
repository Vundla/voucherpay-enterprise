# VoucherPay Enterprise - Setup Guide

## 🚀 Quick Start

This guide will help you set up the VoucherPay Enterprise platform on your local machine with full accessibility features enabled.

### Prerequisites

- **Node.js** 18+ 
- **Python** 3.9+
- **Docker** and **Docker Compose** (recommended)
- **MariaDB** 10.9+
- **Redis** 7+

### Environment Setup

1. **Clone the repository**
```bash
git clone https://github.com/Vundla/voucherpay-enterprise.git
cd voucherpay-enterprise
```

2. **Environment Configuration**
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. **Docker Setup (Recommended)**
```bash
docker-compose up -d
```

Or run services individually:

### FastAPI Backend Setup

```bash
cd backend/fastapi
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Node.js Backend Setup

```bash
cd backend/nodejs
npm install
npm run dev
```

### Angular Frontend Setup

```bash
cd frontend/angular
npm install
npm start
```

## 🌟 Accessibility Features

### WCAG 2.1 AA Compliance

The platform is designed with accessibility at its core:

- **Screen Reader Support**: Compatible with NVDA, JAWS, VoiceOver, TalkBack
- **Keyboard Navigation**: Full keyboard accessibility with logical tab order
- **High Contrast**: Built-in high contrast themes
- **Text Scaling**: Support for up to 200% zoom
- **Voice Control**: Compatible with Dragon NaturallySpeaking and Voice Control

### Accessibility Testing

```bash
# Frontend accessibility audit
cd frontend/angular
npm run accessibility:audit

# Run axe accessibility tests
npm run accessibility:test
```

### Screen Reader Instructions

1. **Navigation**: Use Tab/Shift+Tab to move between elements
2. **Skip Links**: Alt+1 (main content), Alt+2 (navigation), Alt+3 (accessibility menu)
3. **Screen Reader Mode**: Toggle with Ctrl+Alt+S
4. **High Contrast**: Toggle with Ctrl+Alt+H

## 💪 Empowerment Features

### Social Security Assistance
- Streamlined benefits application process
- Document upload with accessibility support
- Status tracking with screen reader optimization

### Accessible Housing Resources
- Housing search with accessibility filters
- Accommodation request system
- Virtual tours with audio descriptions

### Business Funding for People with Disabilities
- Specialized grant database
- Application assistance with accessibility support
- Mentor matching system

### Non-Discrimination Reporting
- Anonymous reporting system
- Accessible complaint forms
- Advocacy resource center

### AI-Powered Assistance
- Accessibility recommendations
- Personalized empowerment suggestions
- Voice-activated help system

## 🔧 Configuration

### Database Configuration

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=voucherpay_enterprise
DB_USER=voucherpay_user
DB_PASSWORD=your_secure_password
```

### Accessibility Configuration

```env
ACCESSIBILITY_AUDIT_ENABLED=true
WCAG_COMPLIANCE_LEVEL=AA
ACCESSIBILITY_LOG_LEVEL=INFO
```

### Email Configuration

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
EMAIL_FROM=noreply@voucherpay.com
```

### OAuth Configuration

```env
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret
LINKEDIN_CLIENT_ID=your_linkedin_client_id
LINKEDIN_CLIENT_SECRET=your_linkedin_client_secret
```

## 🔐 Authentication & Security

### Two-Factor Authentication (2FA)

1. **Setup**: Navigate to Settings > Security > Two-Factor Authentication
2. **Scan QR Code**: Use authenticator app or manual entry
3. **Backup Codes**: Save backup codes in secure location
4. **Accessibility**: QR code alternatives and audio instructions available

### Social Login

Supported platforms:
- Google OAuth 2.0
- GitHub OAuth
- LinkedIn OAuth

## 📊 Analytics & Monitoring

### Empowerment Impact Tracking

The platform tracks:
- Barrier reduction metrics
- Opportunity access rates
- Support provision effectiveness
- Accessibility feature usage

### Real-Time Analytics

```bash
# Access analytics dashboard
http://localhost:4200/analytics

# API analytics endpoint
http://localhost:8000/api/v1/analytics
```

## 🚢 Deployment

### Production Deployment

```bash
# Build all services
docker-compose -f docker-compose.prod.yml up -d

# Or build individually
npm run build:prod  # Frontend
npm run build       # Node.js backend
# FastAPI is built in Docker
```

### Environment Variables for Production

```env
NODE_ENV=production
ENVIRONMENT=production
DEBUG=false
```

## 🧪 Testing

### Unit Tests
```bash
# FastAPI tests
cd backend/fastapi
pytest

# Node.js tests  
cd backend/nodejs
npm test

# Angular tests
cd frontend/angular
npm test
```

### Accessibility Tests
```bash
# Pa11y accessibility testing
npm run accessibility:audit

# axe-core testing
npm run accessibility:test
```

### Integration Tests
```bash
# End-to-end tests with accessibility checks
npm run e2e:a11y
```

## 🔧 Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Check MariaDB is running
   - Verify database credentials
   - Ensure database exists

2. **Screen Reader Not Working**
   - Check browser compatibility
   - Verify ARIA attributes
   - Test with multiple screen readers

3. **High Contrast Mode Issues**
   - Clear browser cache
   - Check CSS custom properties
   - Verify theme configuration

### Getting Help

- **Documentation**: `/docs` endpoint
- **Accessibility Support**: accessibility@voucherpay.com
- **Community Forum**: https://community.voucherpay.com
- **GitHub Issues**: https://github.com/Vundla/voucherpay-enterprise/issues

## 📚 Additional Resources

- [Accessibility Guidelines](docs/accessibility.md)
- [Empowerment Features](docs/empowerment.md)
- [API Documentation](docs/api.md)
- [Contributing Guide](docs/contributing.md)
- [Security Guide](docs/security.md)
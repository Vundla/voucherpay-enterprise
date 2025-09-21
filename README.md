# VoucherPay Enterprise - Inclusive Platform

A comprehensive full-stack platform designed with accessibility and empowerment at its core, specifically created to support and empower people with disabilities through fair access to social security, housing, business funding, and non-discrimination initiatives.

## 🌟 Mission Statement

VoucherPay Enterprise is committed to creating an inclusive digital ecosystem that breaks down barriers and empowers people with disabilities. Our platform provides equal access to opportunities, resources, and services while maintaining the highest standards of accessibility and user experience.

## ✨ Key Features

### Empowerment-Focused Modules
- **Social Security Assistance**: Streamlined access to benefits and support services
- **Accessible Housing Resources**: Housing search with accessibility filters and support
- **Business Funding for People with Disabilities**: Specialized funding opportunities and resources
- **Non-Discrimination Reporting**: Safe reporting mechanisms and advocacy tools
- **Career Opportunities**: Inclusive job matching with accessibility considerations

### Technical Excellence
- **Full-Stack Architecture**: FastAPI (Python) + Node.js/Express + Angular
- **Real-Time Analytics**: WebSocket-powered dashboards and insights
- **Advanced Authentication**: JWT with 2FA support
- **Social Integration**: LinkedIn, GitHub, Google OAuth
- **Data Export**: Comprehensive CSV/JSON export capabilities
- **WCAG 2.1 AA Compliance**: Full accessibility standards compliance

## 🏗️ Architecture

```
voucherpay-enterprise/
├── backend/
│   ├── fastapi/          # Python FastAPI backend
│   └── nodejs/           # Node.js/Express backend with GraphQL
├── frontend/
│   └── angular/          # Angular frontend application
├── docs/                 # Documentation and guides
└── docker/               # Docker/Podman configurations
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18+
- Docker/Podman
- MariaDB

### Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/Vundla/voucherpay-enterprise.git
cd voucherpay-enterprise
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Start with Docker:
```bash
docker-compose up -d
```

Or run individually:

#### FastAPI Backend
```bash
cd backend/fastapi
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Node.js Backend
```bash
cd backend/nodejs
npm install
npm run dev
```

#### Angular Frontend
```bash
cd frontend/angular
npm install
ng serve
```

## 📋 Modules Overview

### Core Modules
- **Users**: User management with accessibility profiles
- **Jobs**: Inclusive job marketplace
- **Finance**: Financial services and business funding
- **Energy**: Sustainable energy initiatives
- **Carbon**: Carbon footprint tracking and offsetting
- **AI**: AI-powered accessibility assistance
- **Policy**: Policy advocacy and compliance tracking

## 🎯 Accessibility Features

### WCAG 2.1 AA Compliance
- Screen reader compatibility
- Keyboard navigation support
- High contrast modes
- Text scaling and zoom support
- Alternative text for all images
- Descriptive link text and headings

### Inclusive Design Principles
- Multiple input methods support
- Cognitive accessibility considerations
- Motor impairment accommodations
- Visual impairment support
- Hearing impairment support

### Technical Accessibility
- ARIA landmarks and labels
- Semantic HTML structure
- Focus management
- Color contrast compliance
- Responsive design for various devices
- Voice navigation support

## 🔐 Security & Authentication

- JWT tokens with refresh mechanisms
- Two-Factor Authentication (2FA)
- OAuth integration (LinkedIn, GitHub, Google)
- Email verification workflows
- Admin review processes
- Secure API endpoints with rate limiting

## 📊 Analytics & Reporting

- Real-time dashboard analytics
- Accessibility usage metrics
- Empowerment impact tracking
- Custom report generation
- Data export capabilities
- Performance monitoring

## 🔧 API Documentation

- Swagger/OpenAPI documentation
- GraphQL schema documentation
- Accessibility API guidelines
- Integration examples
- Testing endpoints

## 🚢 Deployment

### Docker/Podman Support
- Multi-container setup
- Environment-specific configurations
- Health checks and monitoring
- Scaling configurations

### Cloud Deployment
- AWS/Azure/GCP ready
- Kubernetes manifests
- CI/CD pipeline templates
- Monitoring and logging setup

## 🤝 Contributing

We welcome contributions that enhance accessibility and empowerment features. Please read our [Contributing Guide](docs/CONTRIBUTING.md) and [Accessibility Guidelines](docs/ACCESSIBILITY.md).

### Development Guidelines
1. Follow WCAG 2.1 AA standards
2. Include accessibility tests
3. Document empowerment features
4. Test with assistive technologies
5. Consider cognitive load and usability

## 📚 Documentation

- [Setup Guide](docs/setup.md)
- [API Documentation](docs/api.md)
- [Accessibility Guide](docs/accessibility.md)
- [Empowerment Features](docs/empowerment.md)
- [2FA Setup Guide](docs/2fa.md)
- [Email Templates](docs/email-templates.md)

## 🏆 Empowerment Impact

This platform is designed to create measurable positive impact:
- Increased access to employment opportunities
- Streamlined social security processes
- Enhanced housing accessibility
- Business funding success rates
- Reduced discrimination incidents
- Improved digital inclusion metrics

## 📞 Support & Community

- [User Support](docs/support.md)
- [Accessibility Feedback](mailto:accessibility@voucherpay.com)
- [Community Forum](https://community.voucherpay.com)
- [Empowerment Resources](docs/empowerment-resources.md)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Special thanks to the disability advocacy community, accessibility experts, and all contributors who help make this platform truly inclusive and empowering.

---

*Building bridges, breaking barriers, empowering lives.*
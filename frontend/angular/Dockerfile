FROM node:18-alpine as build

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci

# Copy source code
COPY . .

# Build the application
RUN npm run build:prod

# Production stage
FROM nginx:alpine

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy built application
COPY --from=build /app/dist/voucherpay-enterprise-frontend /usr/share/nginx/html

# Add accessibility headers and configurations
RUN echo 'add_header X-Accessibility-Compliant "WCAG-2.1-AA";' >> /etc/nginx/conf.d/accessibility.conf && \
    echo 'add_header X-Screen-Reader-Optimized "true";' >> /etc/nginx/conf.d/accessibility.conf && \
    echo 'add_header X-Keyboard-Accessible "true";' >> /etc/nginx/conf.d/accessibility.conf

# Expose port
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/health || exit 1

CMD ["nginx", "-g", "daemon off;"]
import { Request, Response, NextFunction } from 'express';
import { logger } from '../utils/logger';

export const analyticsMiddleware = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  const startTime = Date.now();

  // Extract request information
  const requestInfo = {
    method: req.method,
    url: req.url,
    path: req.path,
    userAgent: req.headers['user-agent'] || '',
    ip: req.ip,
    timestamp: new Date().toISOString(),
    accessibilityContext: (req as any).accessibilityContext || {},
  };

  // Detect empowerment context
  const empowermentContext = {
    social_security: req.path.includes('/social-security') || req.path.includes('/benefits'),
    housing: req.path.includes('/housing') || req.path.includes('/accommodation'),
    business_funding: req.path.includes('/funding') || req.path.includes('/grants'),
    jobs: req.path.includes('/jobs') || req.path.includes('/employment'),
    non_discrimination: req.path.includes('/report') || req.path.includes('/discrimination'),
    accessibility: req.path.includes('/accessibility') || req.path.includes('/wcag'),
    ai_assistance: req.path.includes('/ai') || req.path.includes('/assistance'),
  };

  // Store analytics data in request
  (req as any).analyticsData = {
    requestInfo,
    empowermentContext,
    startTime,
  };

  // Override response end to capture response data
  const originalEnd = res.end;
  res.end = function(chunk?: any, encoding?: any) {
    const responseTime = Date.now() - startTime;
    
    // Log analytics event
    const analyticsEvent = {
      ...requestInfo,
      empowermentContext,
      response: {
        statusCode: res.statusCode,
        responseTime,
        success: res.statusCode >= 200 && res.statusCode < 400,
      },
      empowermentMetrics: {
        featuresAccessed: Object.values(empowermentContext).filter(Boolean).length,
        accessibilityUsed: Object.values(requestInfo.accessibilityContext).some(Boolean),
        impactIndicators: {
          barrierReduced: res.statusCode < 400 && Object.values(empowermentContext).some(Boolean),
          opportunityAccessed: res.statusCode < 400 && (empowermentContext.jobs || empowermentContext.business_funding),
          supportProvided: res.statusCode < 400 && (empowermentContext.ai_assistance || empowermentContext.accessibility),
        },
      },
    };

    // Log the event (in production, this would go to analytics service)
    if (req.path !== '/health' && req.path !== '/favicon.ico') {
      logger.info(`Analytics Event: ${JSON.stringify(analyticsEvent)}`);
    }

    return originalEnd.call(this, chunk, encoding);
  };

  next();
};
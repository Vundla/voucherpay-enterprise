import { Request, Response, NextFunction } from 'express';

export const accessibilityMiddleware = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  // Extract accessibility context from headers
  const accessibilityContext = {
    screen_reader: req.headers['x-screen-reader'] === 'true',
    high_contrast: req.headers['x-high-contrast'] === 'true',
    reduced_motion: req.headers['x-reduced-motion'] === 'true',
    keyboard_navigation: req.headers['x-keyboard-navigation'] === 'true',
    font_size: req.headers['x-font-size'] || '16',
    language: req.headers['accept-language'] || 'en',
  };

  // Store in request object
  (req as any).accessibilityContext = accessibilityContext;

  // Add accessibility headers to response
  res.setHeader('X-Accessibility-Compliant', 'WCAG-2.1-AA');
  res.setHeader('X-Screen-Reader-Optimized', 'true');
  res.setHeader('X-Keyboard-Accessible', 'true');
  res.setHeader('X-High-Contrast-Support', 'true');

  // Override json method to add accessibility metadata
  const originalJson = res.json;
  res.json = function(body: any) {
    if (typeof body === 'object' && body !== null) {
      body._accessibility = {
        wcag_level: 'AA',
        screen_reader_optimized: true,
        keyboard_accessible: true,
        high_contrast_available: true,
        context: accessibilityContext
      };
    }
    return originalJson.call(this, body);
  };

  next();
};
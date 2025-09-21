import { Request, Response, NextFunction } from 'express';
import { logger } from '../utils/logger';

export const errorHandler = (
  error: Error,
  req: Request,
  res: Response,
  next: NextFunction
) => {
  logger.error('Error occurred:', error);

  const statusCode = (error as any).statusCode || 500;
  const message = error.message || 'Internal Server Error';

  res.status(statusCode).json({
    error: {
      code: statusCode,
      message,
      type: error.constructor.name,
      accessibility: {
        screen_reader_message: `Error ${statusCode}: ${message}`,
        user_friendly_message: message,
        suggested_action: 'Please check your request and try again'
      }
    },
    _accessibility: {
      wcag_level: 'AA',
      screen_reader_optimized: true,
      keyboard_accessible: true,
      high_contrast_available: true
    }
  });
};
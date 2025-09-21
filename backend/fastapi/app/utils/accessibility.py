from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Callable, Any, Dict
import time
import logging

logger = logging.getLogger(__name__)


class AccessibilityMiddleware(BaseHTTPMiddleware):
    """
    Middleware to enhance API responses with accessibility features
    """
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Add accessibility context to request
        request.state.accessibility_context = self._get_accessibility_context(request)
        
        # Process request
        response = await call_next(request)
        
        # Enhance response with accessibility features
        if isinstance(response, JSONResponse):
            response = await self._enhance_json_response(request, response)
        
        # Add accessibility headers
        self._add_accessibility_headers(response)
        
        return response
    
    def _get_accessibility_context(self, request: Request) -> Dict[str, Any]:
        """Extract accessibility context from request headers"""
        return {
            "screen_reader": request.headers.get("X-Screen-Reader") == "true",
            "high_contrast": request.headers.get("X-High-Contrast") == "true",
            "reduced_motion": request.headers.get("X-Reduced-Motion") == "true",
            "keyboard_navigation": request.headers.get("X-Keyboard-Navigation") == "true",
            "font_size": request.headers.get("X-Font-Size", "16"),
            "language": request.headers.get("Accept-Language", "en"),
            "user_agent": request.headers.get("User-Agent", ""),
        }
    
    async def _enhance_json_response(self, request: Request, response: JSONResponse) -> JSONResponse:
        """Enhance JSON response with accessibility information"""
        try:
            content = response.body.decode() if response.body else "{}"
            import json
            data = json.loads(content)
            
            # Add accessibility metadata
            if isinstance(data, dict):
                accessibility_context = getattr(request.state, "accessibility_context", {})
                
                data["_accessibility"] = {
                    "wcag_level": "AA",
                    "screen_reader_optimized": True,
                    "keyboard_accessible": True,
                    "high_contrast_available": True,
                    "context": accessibility_context
                }
                
                # Add screen reader friendly messages for errors
                if "error" in data:
                    error = data["error"]
                    if isinstance(error, dict) and "message" in error:
                        error["screen_reader_message"] = self._create_screen_reader_message(error["message"])
                        error["user_friendly_message"] = self._create_user_friendly_message(error["message"])
            
            # Create new response with enhanced content
            new_response = JSONResponse(
                content=data,
                status_code=response.status_code,
                headers=dict(response.headers)
            )
            return new_response
            
        except Exception as e:
            logger.warning(f"Failed to enhance response with accessibility features: {e}")
            return response
    
    def _add_accessibility_headers(self, response: Response) -> None:
        """Add accessibility-related headers to response"""
        response.headers["X-Accessibility-Compliant"] = "WCAG-2.1-AA"
        response.headers["X-Screen-Reader-Optimized"] = "true"
        response.headers["X-Keyboard-Accessible"] = "true"
        response.headers["X-High-Contrast-Support"] = "true"
        response.headers["X-Content-Language"] = "en"
    
    def _create_screen_reader_message(self, message: str) -> str:
        """Create screen reader optimized message"""
        # Convert technical messages to screen reader friendly format
        screen_reader_replacements = {
            "401": "Authentication required. Please log in to continue.",
            "403": "Access denied. You don't have permission for this action.",
            "404": "The requested resource was not found.",
            "422": "The submitted data contains errors. Please check and try again.",
            "500": "A server error occurred. Please try again later or contact support."
        }
        
        for code, friendly_message in screen_reader_replacements.items():
            if code in message:
                return friendly_message
        
        return message
    
    def _create_user_friendly_message(self, message: str) -> str:
        """Create user-friendly message"""
        user_friendly_replacements = {
            "validation error": "Please check the information you entered and try again.",
            "unauthorized": "Please sign in to access this feature.",
            "forbidden": "You don't have permission to perform this action.",
            "not found": "The item you're looking for couldn't be found.",
            "internal server error": "Something went wrong. Please try again in a moment."
        }
        
        message_lower = message.lower()
        for trigger, friendly_message in user_friendly_replacements.items():
            if trigger in message_lower:
                return friendly_message
        
        return message
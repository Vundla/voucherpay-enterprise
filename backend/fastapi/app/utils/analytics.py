from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Callable, Dict, Any
import time
import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class AnalyticsMiddleware(BaseHTTPMiddleware):
    """
    Middleware to collect analytics data for empowerment tracking
    """
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        start_time = time.time()
        
        # Extract request information
        request_info = self._extract_request_info(request)
        
        # Process request
        response = await call_next(request)
        
        # Calculate response time
        process_time = time.time() - start_time
        
        # Extract response information
        response_info = self._extract_response_info(response, process_time)
        
        # Log analytics event
        await self._log_analytics_event(request_info, response_info, request)
        
        return response
    
    def _extract_request_info(self, request: Request) -> Dict[str, Any]:
        """Extract relevant information from request"""
        return {
            "method": request.method,
            "url": str(request.url),
            "path": request.url.path,
            "query_params": dict(request.query_params),
            "user_agent": request.headers.get("User-Agent", ""),
            "ip_address": request.client.host if request.client else None,
            "timestamp": datetime.utcnow().isoformat(),
            "accessibility": {
                "screen_reader": request.headers.get("X-Screen-Reader") == "true",
                "high_contrast": request.headers.get("X-High-Contrast") == "true",
                "keyboard_navigation": request.headers.get("X-Keyboard-Navigation") == "true",
                "reduced_motion": request.headers.get("X-Reduced-Motion") == "true",
            },
            "empowerment_context": self._detect_empowerment_context(request.url.path)
        }
    
    def _extract_response_info(self, response: Response, process_time: float) -> Dict[str, Any]:
        """Extract relevant information from response"""
        return {
            "status_code": response.status_code,
            "process_time": process_time,
            "headers": dict(response.headers),
            "success": 200 <= response.status_code < 400
        }
    
    def _detect_empowerment_context(self, path: str) -> Dict[str, bool]:
        """Detect which empowerment features are being accessed"""
        empowerment_patterns = {
            "social_security": any(pattern in path for pattern in ["/social-security", "/benefits", "/assistance"]),
            "housing": any(pattern in path for pattern in ["/housing", "/accommodation", "/accessibility-housing"]),
            "business_funding": any(pattern in path for pattern in ["/funding", "/grants", "/business-support"]),
            "jobs": any(pattern in path for pattern in ["/jobs", "/employment", "/careers"]),
            "non_discrimination": any(pattern in path for pattern in ["/report", "/discrimination", "/advocacy"]),
            "accessibility": any(pattern in path for pattern in ["/accessibility", "/wcag", "/assistive"]),
            "ai_assistance": any(pattern in path for pattern in ["/ai", "/assistance", "/recommendations"])
        }
        return empowerment_patterns
    
    async def _log_analytics_event(self, request_info: Dict[str, Any], response_info: Dict[str, Any], request: Request) -> None:
        """Log analytics event for tracking empowerment impact"""
        try:
            analytics_data = {
                "event_type": "api_request",
                "request": request_info,
                "response": response_info,
                "user_id": getattr(request.state, "user_id", None),
                "session_id": request.headers.get("X-Session-ID"),
                "empowerment_metrics": self._calculate_empowerment_metrics(request_info, response_info)
            }
            
            # Log to analytics system (could be database, external service, etc.)
            logger.info(f"Analytics Event: {json.dumps(analytics_data, default=str)}")
            
            # Store in database if needed
            # await self._store_analytics_event(analytics_data)
            
        except Exception as e:
            logger.error(f"Failed to log analytics event: {e}")
    
    def _calculate_empowerment_metrics(self, request_info: Dict[str, Any], response_info: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate metrics related to empowerment features"""
        empowerment_context = request_info.get("empowerment_context", {})
        accessibility_context = request_info.get("accessibility", {})
        
        metrics = {
            "accessibility_usage": {
                "screen_reader_used": accessibility_context.get("screen_reader", False),
                "high_contrast_used": accessibility_context.get("high_contrast", False),
                "keyboard_navigation_used": accessibility_context.get("keyboard_navigation", False),
                "accessibility_score": sum(accessibility_context.values()) / len(accessibility_context) if accessibility_context else 0
            },
            "empowerment_engagement": {
                "features_accessed": sum(empowerment_context.values()),
                "social_security_accessed": empowerment_context.get("social_security", False),
                "housing_accessed": empowerment_context.get("housing", False),
                "funding_accessed": empowerment_context.get("business_funding", False),
                "jobs_accessed": empowerment_context.get("jobs", False),
                "advocacy_accessed": empowerment_context.get("non_discrimination", False)
            },
            "performance": {
                "response_time": response_info.get("process_time", 0),
                "success": response_info.get("success", False),
                "status_code": response_info.get("status_code", 500)
            },
            "impact_indicators": {
                "barrier_reduced": self._detect_barrier_reduction(request_info, response_info),
                "opportunity_accessed": self._detect_opportunity_access(request_info, response_info),
                "support_provided": self._detect_support_provision(request_info, response_info)
            }
        }
        
        return metrics
    
    def _detect_barrier_reduction(self, request_info: Dict[str, Any], response_info: Dict[str, Any]) -> bool:
        """Detect if the request helped reduce barriers for users with disabilities"""
        accessibility_used = any(request_info.get("accessibility", {}).values())
        empowerment_accessed = any(request_info.get("empowerment_context", {}).values())
        success = response_info.get("success", False)
        
        return accessibility_used and empowerment_accessed and success
    
    def _detect_opportunity_access(self, request_info: Dict[str, Any], response_info: Dict[str, Any]) -> bool:
        """Detect if the request provided access to opportunities"""
        opportunity_paths = ["/jobs", "/funding", "/housing", "/grants"]
        path = request_info.get("path", "")
        success = response_info.get("success", False)
        
        return any(opp_path in path for opp_path in opportunity_paths) and success
    
    def _detect_support_provision(self, request_info: Dict[str, Any], response_info: Dict[str, Any]) -> bool:
        """Detect if the request provided support or assistance"""
        support_paths = ["/assistance", "/support", "/help", "/ai", "/recommendations"]
        path = request_info.get("path", "")
        success = response_info.get("success", False)
        
        return any(support_path in path for support_path in support_paths) and success
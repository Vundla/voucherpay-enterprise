from fastapi import APIRouter, Depends
from typing import Any, Dict
from app.core.security import get_current_user_token

router = APIRouter()

@router.get("/", response_model=Dict[str, Any])
async def get_finance_overview(
    current_user: Dict[str, Any] = Depends(get_current_user_token)
) -> Dict[str, Any]:
    """Get financial services and business funding opportunities"""
    return {
        "message": "Finance endpoint - Business funding and financial empowerment",
        "empowerment_features": ["disability_business_grants", "accessible_banking", "financial_assistance"]
    }
from datetime import datetime, timedelta
from typing import Optional, Any, Dict
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import pyotp
import qrcode
from io import BytesIO
import base64

from app.core.config import settings

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Token security
security = HTTPBearer()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against its hash"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a password for storing"""
    return pwd_context.hash(password)


def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """
    Create JWT access token
    
    Args:
        data: Token payload data
        expires_delta: Token expiration time
        
    Returns:
        Encoded JWT token
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: Dict[str, Any]) -> str:
    """
    Create JWT refresh token
    
    Args:
        data: Token payload data
        
    Returns:
        Encoded JWT refresh token
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> Dict[str, Any]:
    """
    Verify and decode JWT token
    
    Args:
        token: JWT token to verify
        
    Returns:
        Decoded token payload
        
    Raises:
        HTTPException: If token is invalid or expired
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def get_current_user_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Dict[str, Any]:
    """
    Get current user from JWT token
    
    Args:
        credentials: HTTP authorization credentials
        
    Returns:
        User information from token
    """
    token = credentials.credentials
    payload = verify_token(token)
    
    if payload.get("type") != "access":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token type",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return payload


def generate_totp_secret() -> str:
    """Generate TOTP secret for 2FA"""
    return pyotp.random_base32()


def generate_totp_qr_code(user_email: str, secret: str) -> str:
    """
    Generate QR code for TOTP setup
    
    Args:
        user_email: User's email address
        secret: TOTP secret
        
    Returns:
        Base64 encoded QR code image
    """
    totp_uri = pyotp.totp.TOTP(secret).provisioning_uri(
        name=user_email,
        issuer_name=settings.TOTP_ISSUER
    )
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(totp_uri)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    
    qr_code_base64 = base64.b64encode(buffer.getvalue()).decode()
    return qr_code_base64


def verify_totp_token(secret: str, token: str) -> bool:
    """
    Verify TOTP token
    
    Args:
        secret: User's TOTP secret
        token: TOTP token to verify
        
    Returns:
        True if token is valid, False otherwise
    """
    totp = pyotp.TOTP(secret)
    return totp.verify(token)


def create_password_reset_token(email: str) -> str:
    """
    Create password reset token
    
    Args:
        email: User's email address
        
    Returns:
        Password reset token
    """
    delta = timedelta(hours=1)  # Token expires in 1 hour
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email, "type": "password_reset"},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    """
    Verify password reset token
    
    Args:
        token: Password reset token
        
    Returns:
        Email if token is valid, None otherwise
    """
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        if decoded_token.get("type") != "password_reset":
            return None
        return decoded_token.get("sub")
    except JWTError:
        return None
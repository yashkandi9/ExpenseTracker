from fastapi import Header, HTTPException
from jose import jwt, JWTError
import requests
import time
from fastapi import APIRouter

router = APIRouter()


# Clerk Config - Replace these
CLERK_ISSUER = "https://fun-dogfish-60.clerk.accounts.dev"  # Ensure this is the correct issuer
JWKS_URL = f"{CLERK_ISSUER}/.well-known/jwks.json"
AUTHORIZED_PARTIES = ["http://localhost:5173"]  # Replace with your authorized parties
AUDIENCE = "http://localhost:5173"  # Replace with your front-end URL or client ID

# Load JWKS from Clerk
try:
    jwks = requests.get(JWKS_URL).json()
except requests.RequestException as e:
    raise RuntimeError(f"Failed to fetch JWKS from {JWKS_URL}: {e}")

def verify_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization format")

    token = authorization.split(" ")[1]

    try:
        # Decode token header without verifying the signature to extract the 'kid'
        unverified_header = jwt.get_unverified_header(token)
        
        # Find the key that matches the 'kid'
        key = next((k for k in jwks["keys"] if k["kid"] == unverified_header["kid"]), None)
        if not key:
            raise HTTPException(status_code=401, detail="Key not found in JWKS")

        # Decode the JWT payload using the key
        payload = jwt.decode(
            token,
            key,
            algorithms=["RS256"],
            audience=AUDIENCE,
            issuer=CLERK_ISSUER,
        )

        # Optional: Validate 'azp' claim for authorized origins (good for security)
        if "azp" in payload and payload["azp"] not in AUTHORIZED_PARTIES:
            raise HTTPException(status_code=401, detail="Invalid authorized party (azp)")

        # Optional: Check for expiration (exp) and not before (nbf) claims
        now = int(time.time())
        if payload.get("exp", now) < now or payload.get("nbf", now) > now:
            raise HTTPException(status_code=401, detail="Token expired or not yet valid")

        # Return the user ID (subject) from the payload
        return payload["sub"]

    except JWTError as e:
        raise HTTPException(status_code=401, detail="Invalid token") from e

from fastapi import APIRouter
from src.infrastructure.config import build_health_use_cases


router = APIRouter()
use_cases = build_health_use_cases()

@router.get("/healthz")
def healthz():
    """Kubernetes liveness probe endpoint."""
    result = use_cases.get_liveness()
    return {"status": "ok" if result.healthy else "fail", "details": result.details}

@router.get("/readyz")
def readyz():
    """Kubernetes readiness probe endpoint."""
    result = use_cases.get_readiness()
    return {"status": "ready" if result.healthy else "not_ready", "details": result.details}

@router.get("/startupz")
def startupz():
    """Kubernetes startup probe endpoint."""
    result = use_cases.get_startup()
    return {"status": "started" if result.healthy else "failed"}

from src.infrastructure.checks.db_checker import DBChecker
from src.domain.health_service import HealthService
from src.application.health_use_cases import HealthUseCases

def build_health_use_cases() -> HealthUseCases:
    """
    Constructs the HealthUseCases object and injects infrastructure adapters.
    """
    db = DBChecker()
    service = HealthService(db_checker=db)
    return HealthUseCases(service)

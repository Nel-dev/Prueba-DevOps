from src.domain.health_service import HealthService

class HealthUseCases:
    """
    Application layer that exposes health operations to adapters.

    It calls domain services and formats responses if needed.
    """

    def __init__(self, health_service: HealthService):
        self.health_service = health_service

    def get_liveness(self):
        """Returns a liveness check result."""
        return self.health_service.liveness()

    def get_readiness(self):
        """Returns a readiness check result."""
        return self.health_service.readiness()

    def get_startup(self):
        """Returns a startup check result."""
        return self.health_service.startup()

class HealthStatus:
    """
    Represents the result of a health check.

    Attributes:
        healthy (bool): Whether the check passed.
        details (dict): Extra information about the check result.
    """
    def __init__(self, healthy: bool, details: dict | None = None):
        self.healthy = healthy
        self.details = details or {}


class HealthService:
    """
    Core domain service that defines system health logic.

    This service knows NOTHING about frameworks, databases,
    or infrastructure details. It only orchestrates checks.
    """

    def __init__(self, db_checker=None):
        self.db_checker = db_checker

    def liveness(self) -> HealthStatus:
        """Checks if the application process is alive."""
        return HealthStatus(True)

    def readiness(self) -> HealthStatus:
        """
        Checks whether required dependencies are ready.

        If no checkers are defined, it's considered ready.
        """
        details = {}

        if self.db_checker:
            details["database"] = self.db_checker.check()

        healthy = all(d.get("ok") for d in details.values()) if details else True
        return HealthStatus(healthy, details)

    def startup(self) -> HealthStatus:
        """Checks if the app has finished its initialization state."""
        return HealthStatus(True)

from domain.health_service import HealthService, HealthStatus

def test_liveness():
    service = HealthService()
    result = service.liveness()
    assert isinstance(result, HealthStatus)
    assert result.healthy is True

def test_readiness_no_dependencies():
    service = HealthService()
    result = service.readiness()
    assert result.healthy is True
    assert result.details == {}

def test_readiness_with_db_ok():
    class FakeDB:
        def check(self):
            return {"ok": True}

    service = HealthService(db_checker=FakeDB())
    result = service.readiness()
    assert result.healthy is True
    assert result.details["database"]["ok"] is True

def test_readiness_with_db_fail():
    class FakeDB:
        def check(self):
            return {"ok": False}

    service = HealthService(db_checker=FakeDB())
    result = service.readiness()
    assert result.healthy is False

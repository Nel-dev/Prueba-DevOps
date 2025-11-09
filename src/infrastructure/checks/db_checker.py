class DBChecker:
    """
    Infrastructure adapter that checks a database connection.

    Replace the implementation with your own DB ping logic.
    """

    def check(self) -> dict:
        # Dummy implementation, always OK.
        return {"ok": True, "message": "DB reachable"}

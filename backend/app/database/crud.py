from app.database.database import SessionLocal
from app.database.models import Scan


def save_scan(result, message):

    db = SessionLocal()

    scan = Scan(
        message=message,
        threat_level=result["threat_level"],
        attack_type=result["attack_type"],
        confidence=result["confidence"],
        risk_score=result["risk_score"]
    )

    db.add(scan)

    db.commit()

    db.close()
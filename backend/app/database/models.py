from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base


class Scan(Base):

    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, index=True)

    message = Column(Text)

    threat_level = Column(String)

    attack_type = Column(String)

    confidence = Column(Integer)

    risk_score = Column(Integer)
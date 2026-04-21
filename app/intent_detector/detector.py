def detect_intent(intent: str) -> str:
    """
    Detect and validate user intent.

    Allowed:
    - REPORTING
    - ML_TRAINING
    - COMPLIANCE
    - RESEARCH
    """

    allowed = {
        "reporting": "REPORTING",
        "ml_training": "ML_TRAINING",
        "compliance": "COMPLIANCE",
        "research": "RESEARCH"
    }

    if not intent:
        raise ValueError("Intent not provided")

    key = intent.strip().lower()

    if key not in allowed:
        raise ValueError(f"Unsupported intent: {intent}")

    return allowed[key]

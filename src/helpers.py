# src/helpers.py - simple mapping used by tests
def code_to_text(code: int) -> str:
    mapping = {
        0: "Clear",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
    }
    return mapping.get(code, "Unknown")

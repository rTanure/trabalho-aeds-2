from pathlib import Path

def verify_existent_file(filepath: str):
    filepath = Path(filepath)
    if not filepath:
        return False
    return True

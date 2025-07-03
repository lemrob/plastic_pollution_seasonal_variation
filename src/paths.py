import os

def get_data_path(filename: str) -> str:
    """
    Returns the full path to a file in the data/ directory,
    regardless of where the script is called from.
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    return os.path.join(base_dir, filename)

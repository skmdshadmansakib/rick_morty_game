import importlib

def load_class(class_path: str):
    """
    Dynamically import a class from a string path like:
    'morties.classic_morty.ClassicMorty'
    """
    module_name, class_name = class_path.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)
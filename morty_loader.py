import importlib

class MortyLoader:
    @staticmethod
    def load(class_path, num_boxes):
        try:
            module_name, class_name = class_path.rsplit('.', 1)
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
            return cls(num_boxes)  # return instance
        except (ImportError, AttributeError, TypeError) as e:
            print(f"Error loading Morty: {e}")
            return None
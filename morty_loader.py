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

            morty_class = getattr(module, class_name)
            return morty_class(num_boxes)
        except Exception as e:
            print(f"Error: Can't import module '{class_path}': {e}")
            exit(1)


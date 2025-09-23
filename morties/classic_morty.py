class ClassicMorty:
    def __init__(self, num_boxes):
        self.num_boxes = num_boxes

    def remove_boxes(self, final_value, rick_guess):
        # Never remove the portal gun box
        return [i for i in range(self.num_boxes) if i != final_value]
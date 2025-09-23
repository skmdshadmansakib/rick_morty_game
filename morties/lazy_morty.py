class LazyMorty:
    def __init__(self, num_boxes):
        self.num_boxes = num_boxes

    def remove_boxes(self, final_value, rick_guess):
        # Remove boxes with the lowest indices, except portal gun
        return [i for i in range(self.num_boxes) if i != final_value]
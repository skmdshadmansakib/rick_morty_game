class ClassicMorty:
    def __init__(self, num_boxes):
        self.num_boxes = num_boxes

    def probability_if_switch(self):
        return 1/self.num_boxes
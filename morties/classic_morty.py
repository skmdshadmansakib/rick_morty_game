class ClassicMorty:
    def __init__(self, num_boxes):
        self.num_boxes = num_boxes

    def remove_boxes(self, num_boxes, guess, gun_location):
        boxes = set(range(num_boxes))
        # always leave original guess + gun box
        boxes.discard(guess)
        boxes.discard(gun_location)
        # leave one other box if needed
        if len(boxes) > 0:
            return {guess, gun_location}
        return {guess}
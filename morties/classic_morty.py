from provably_fair import ProvablyFair

class ClassicMorty:
    def __init__(self, num_boxes):
        self.num_boxes = num_boxes
        self.number = None
        self.key = None
        self.hmac_val = None

    def generate_hmac(self):
        self.number, self.key, self.hmac_val = ProvablyFair.generate_number(self.num_boxes)
        return self.hmac_val

    def finalize_number(self):
        return self.number, self.key

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


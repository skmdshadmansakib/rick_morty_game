from provably_fair import ProvablyFair

class LazyMorty:
    def __init__(self, num_boxes):
        self.num_boxes = num_boxes
        self.number = None
        self.key = None
        self.hmac_val = None

    def generate_hmac(self):
        # LazyMorty favors high numbers sometimes
        import random
        self.number, self.key, self.hmac_val = ProvablyFair.generate_number(self.num_boxes)
        if random.random() > 0.5:
            self.number = (self.number + 1) % self.num_boxes
        return self.hmac_val

    def finalize_number(self):
        return self.number, self.key
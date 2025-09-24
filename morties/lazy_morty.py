class LazyMorty:
    def __init__(self, num_boxes):
        self.num_boxes = num_boxes

    def remove_boxes(self, num_boxes, guess, gun_location):
        # removes boxes with lowest indices except gun box
        boxes = set(range(num_boxes))
        boxes.discard(gun_location)
        boxes = set(sorted(boxes)[1:])  # leave only one other box
        return {gun_location}.union(boxes)
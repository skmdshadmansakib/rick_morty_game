import secrets
import hmac
import hashlib

class ProvablyFair:
    def __init__(self, num_boxes):
        self.num_boxes = num_boxes
        self.secret_key = secrets.token_bytes(32)
        self.morty_value = secrets.randbelow(num_boxes)
        self.final = (self.morty_value + secrets.randbelow(num_boxes)) % num_boxes  # final directly sets gun

    def get_hmac(self):
        return hmac.new(self.secret_key, str(self.morty_value).encode(), hashlib.sha3_256).hexdigest()

    def reveal(self):
        # Returns morty_value, key, gun_location
        return self.morty_value, self.secret_key.hex(), self.final
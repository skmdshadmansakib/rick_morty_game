import secrets
import hmac
import hashlib

class ProvablyFair:
    def __init__(self, num_boxes):
        self.num_boxes = num_boxes
        self.secret_key = secrets.token_bytes(32)  # 256-bit key
        self.morty_value = secrets.randbelow(num_boxes)

    def get_hmac(self):
        return hmac.new(self.secret_key, str(self.morty_value).encode(), hashlib.sha3_256).hexdigest()

    def reveal(self):
        return self.morty_value, self.secret_key
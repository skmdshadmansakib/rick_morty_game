import hmac
import hashlib
import secrets

class ProvablyFair:
    @staticmethod
    def generate_number(num_boxes):
        """Return random number and secret key"""
        key = secrets.token_hex(32)
        number = secrets.randbelow(num_boxes)
        hmac_val = hmac.new(key.encode(), str(number).encode(), hashlib.sha256).hexdigest()
        return number, key, hmac_val

    @staticmethod
    def verify_number(number, key, hmac_val):
        """Verify HMAC"""
        calc_hmac = hmac.new(key.encode(), str(number).encode(), hashlib.sha256).hexdigest()
        return hmac.compare_digest(calc_hmac, hmac_val)
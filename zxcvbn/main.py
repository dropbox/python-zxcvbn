from matching import omnimatch
from scoring import minimum_entropy_match_sequence
import time

def password_strength(password, user_inputs=[]):
    start = time.time()
    matches = omnimatch(password, user_inputs)
    result = minimum_entropy_match_sequence(password, matches)
    result['calc_time'] = time.time() - start
    return result

import time
from google.api_core.exceptions import ResourceExhausted

def call_with_retry(fn, *args, max_retries=3, base_delay=5, **kwargs):
    for attempt in range(max_retries):
        try:
            return fn(*args, **kwargs)
        except ResourceExhausted:
            if attempt == max_retries - 1:
                raise
            time.sleep(base_delay * (attempt + 1))
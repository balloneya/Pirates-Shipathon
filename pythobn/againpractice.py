from typing import Callable
import functools
import time


def timed_logger(func: Callable, log_enabled: bool = True) -> Callable:

    @functools.wraps(func)  # Preserve metadata
    def wrapper(*args, **kwargs):

        start_time = time.time()

        try:
            # 1. Execute the function and store the result
            result = func(*args, **kwargs)

            # 2. Log if enabled
            if log_enabled:
                # FIX: Use func.__name__ to print the name, not the object
                print(
                    f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}")
                print(f"Function {func.__name__} returned: {result}")

            # 3. Return the stored result
            return result

        except Exception as e:
            if log_enabled:
                print(f"Function {func.__name__} raised an exception: {e}")
            raise  # Re-raise the exception

        finally:
            # 4. This *always* runs
            end_time = time.time()
            duration = (end_time - start_time) * 1000
            # FIX: Format the time nicely
            print(f"Execution time: {duration:.2f} ms")

        # Note: The 'return result' is inside the 'try' block.
        # The 'finally' block will run, and *then* the value will be returned.

    return wrapper

# --- Example test functions ---


def slow_add(a, b):
    """ Adds two numbers with a delay ."""
    time.sleep(0.1)
    return a + b


def multiply(a, b):
    """ Multiplies two numbers ."""
    return a * b

# --- Main execution block ---


# FIX: Removed the spaces around "__main__"
if __name__ == "__main__":

    print("--- Testing slow_add (logging enabled) ---")
    slow_add_logged = timed_logger(slow_add, log_enabled=True)
    # Store the returned value so we can see it
    total = slow_add_logged(5, 7)
    print(f"Actual value returned: {total}")

    print("\n--- Testing multiply (logging disabled) ---")
    multiply_logged = timed_logger(multiply, log_enabled=False)
    # Store the returned value so we can see it
    product = multiply_logged(3, 4)
    print(f"Actual value returned: {product}")

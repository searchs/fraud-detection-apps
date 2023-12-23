from loguru import logger


def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x > 2:
        status_false = 0
        for n in range(2, x):
            if x % n == 0:
                status_false += 1

        if status_false == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    # logger.info(is_prime(9207))

    # Testing
    falsy = []
    truthy = []

    for p in range(0, 1001):
        if is_prime(p):
            truthy.append(p)
        else:
            falsy.append(p)

    logger.info(f"Count of Prime Numbers: {len(truthy)}")
    logger.info(f"Count of Non-Prime Numbers: {len(falsy)}")
    # logger.info(truthy)

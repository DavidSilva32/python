# Static Method
import math


class Math:
    @staticmethod
    def sqrt(x):
        return math.sqrt(x)


if __name__ == "__main__":
    m = Math()
    print(m.sqrt(20))

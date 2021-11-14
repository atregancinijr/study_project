

class Utils:

    @staticmethod
    def count_points(matriz):
        points_sum = 0
        for linha in matriz:
            points_sum += linha.count(1)
        return points_sum

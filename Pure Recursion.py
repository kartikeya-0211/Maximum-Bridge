import math

class MaxBridgeRecursion:
    @staticmethod
    def maxBridges(bridges, currentIndex, prevSouth):
        if currentIndex == len(bridges):
            return 0

        # Option 1: Do not take the current bridge
        notTake = MaxBridgeRecursion.maxBridges(bridges, currentIndex + 1, prevSouth)

        # Option 2: Take the current bridge, if possible
        take = 0
        if bridges[currentIndex][1] > prevSouth:
            take = 1 + MaxBridgeRecursion.maxBridges(bridges, currentIndex + 1, bridges[currentIndex][1])

        return max(take, notTake)

    @staticmethod
    def main():
        bridges = [[6, 2], [4, 3], [2, 6], [1, 5]]

        # Sort bridges based on their north bank coordinates
        bridges.sort(key=lambda a: a[0])

        result = MaxBridgeRecursion.maxBridges(bridges, 0, -math.inf) # Use -math.inf for Integer.MIN_VALUE
        print("Max non-crossing bridges (Recursion): " + str(result))

if __name__ == "__main__":
    MaxBridgeRecursion.main()

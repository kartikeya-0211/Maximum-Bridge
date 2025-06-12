import math

class MaxBridgeMemo:
    # Using a class variable for dp table to mimic static behavior
    dp = None

    @staticmethod
    def maxBridges(bridges, currentIndex, prevIndex):
        if currentIndex == len(bridges):
            return 0

        # Adjusting prevIndex for dp table lookup: -1 becomes 0, 0 becomes 1, etc.
        # This is because array indices cannot be negative.
        if MaxBridgeMemo.dp[currentIndex][prevIndex + 1] != -1:
            return MaxBridgeMemo.dp[currentIndex][prevIndex + 1]

        # Option 1: Do not take the current bridge
        notTake = MaxBridgeMemo.maxBridges(bridges, currentIndex + 1, prevIndex)

        # Option 2: Take the current bridge, if possible
        take = 0
        if prevIndex == -1 or bridges[currentIndex][1] > bridges[prevIndex][1]:
            take = 1 + MaxBridgeMemo.maxBridges(bridges, currentIndex + 1, currentIndex)

        MaxBridgeMemo.dp[currentIndex][prevIndex + 1] = max(take, notTake)
        return MaxBridgeMemo.dp[currentIndex][prevIndex + 1]

    @staticmethod
    def main():
        bridges = [[6, 2], [4, 3], [2, 6], [1, 5]]

        # Sort bridges based on their north bank coordinates
        bridges.sort(key=lambda a: a[0])

        n = len(bridges)
        # Initialize dp table with -1
        # The size of the second dimension is n + 1 because prevIndex can range from -1 to n-1.
        # So, prevIndex + 1 will range from 0 to n.
        MaxBridgeMemo.dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

        result = MaxBridgeMemo.maxBridges(bridges, 0, -1)
        print("Max non-crossing bridges (Memoization): " + str(result))

if __name__ == "__main__":
    MaxBridgeMemo.main()

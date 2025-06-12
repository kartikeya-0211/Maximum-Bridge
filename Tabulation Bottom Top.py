import math

class MaxBridgeTabulation:
    @staticmethod
    def maxBridges(bridges):
        # Sort bridges based on their north bank coordinates
        bridges.sort(key=lambda a: a[0])

        n = len(bridges)
        if n == 0:
            return 0
        dp = [1] * n

        maxLen = 1  # Initialize maxLen with at least 1 (for a single bridge)

        # Fill dp array using a nested loop
        for i in range(1, n):
            for j in range(i):
                if bridges[i][1] > bridges[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxLen = max(maxLen, dp[i])

        return maxLen

    @staticmethod
    def main():
        bridges = [[6, 2], [4, 3], [2, 6], [1, 5]]

        result = MaxBridgeTabulation.maxBridges(bridges)
        print("Max non-crossing bridges (Tabulation): " + str(result))

if __name__ == "__main__":
    MaxBridgeTabulation.main()

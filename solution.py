def solve_civil_war(powers):
    n = len(powers)
    if n == 0:
        return 0
    
    # Memoization dictionary
    memo = {}
    
    def dp(left, right, turn):
        """
        Returns the difference in scores (current_player - opponent) 
        for the subarray powers[left:right+1] when it's current player's turn
        turn: 0 for first player, 1 for second player
        """
        if left > right:
            return 0
        
        if (left, right, turn) in memo:
            return memo[(left, right, turn)]
        
        # Try taking consecutive elements from left side
        best_diff = float('-inf')
        current_sum = 0
        
        # Take 1 to (right-left+1) consecutive elements from left
        for i in range(left, right + 1):
            current_sum += powers[i]
            # After taking powers[left:i+1], opponent plays on powers[i+1:right+1]
            opponent_diff = dp(i + 1, right, 1 - turn)
            current_diff = current_sum - opponent_diff
            best_diff = max(best_diff, current_diff)
        
        # Try taking consecutive elements from right side
        current_sum = 0
        
        # Take 1 to (right-left+1) consecutive elements from right
        for i in range(right, left - 1, -1):
            current_sum += powers[i]
            # After taking powers[i:right+1], opponent plays on powers[left:i]
            opponent_diff = dp(left, i - 1, 1 - turn)
            current_diff = current_sum - opponent_diff
            best_diff = max(best_diff, current_diff)
        
        memo[(left, right, turn)] = best_diff
        return best_diff
    
    # First player starts, returns (first_player_score - second_player_score)
    diff = dp(0, n - 1, 0)
    return abs(diff)

def main():
    n = int(input())
    powers = list(map(int, input().split()))
    
    result = solve_civil_war(powers)
    print(result)

if __name__ == "__main__":
    main()
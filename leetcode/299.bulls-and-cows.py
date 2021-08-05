from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        total = success = 0
        secret_counter = Counter(secret)
        guess_counter = Counter(guess)

        for k, v in secret_counter.items():
            if guess_counter[k]:
                total += min(secret_counter[k], guess_counter[k]) 

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                success += 1
        
        return "{0}A{1}B".format(success, total - success)

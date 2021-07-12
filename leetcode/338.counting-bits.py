def countBits(n):
        """
        had the idea of using dp but botched it badly :) sucks to be me.
        """
        count = [0]
        for i in range(1, n+1):
            if i % 2 == 1:
                count.append(count[i-1]+1)
            else:
                count.append(count[i // 2])
        return count
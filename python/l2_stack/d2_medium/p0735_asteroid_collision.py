class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        output = []
        stk = []
        for asteroid in asteroids:
            # stack empty
            if len(stk) == 0:
                if asteroid > 0:
                    stk.append(asteroid)
                else:
                    output.append(asteroid)
            # stack non empty
            else:
                if asteroid > 0:
                    stk.append(asteroid)
                elif asteroid < 0:
                    while stk and abs(asteroid) > stk[-1]:
                        stk.pop()
        return asteroid + stk
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def get_steps(cur, curr_next):
            step = 0
            while cur <= n:
                step += min(n+1, curr_next) - cur
                cur = cur * 10
                curr_next = curr_next * 10
            return step
        
        curr = 1
        k -= 1
        while k > 0:
            s = get_steps(curr, curr+1)
            if s <= k:
                curr += 1
                k -= s
            else:
                curr = curr * 10
                k -= 1
        return curr


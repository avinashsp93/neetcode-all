class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for op in logs:
            if op == "./":
                continue
            elif op == "../":
                if count > 0:
                    count -= 1
            else:
                count += 1
        return count
    
    def minOperations_stackApproach(self, logs: List[str]) -> int:
        log_stack = []
        for op in logs:
            if op == "./":
                continue
            elif op == "../":
                if log_stack:
                    log_stack.pop()
            else:
                log_stack.append(op)
        return len(log_stack)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right, blocks_length = 0, k, len(blocks)
        i = 0
        bw_map = dict()
        while(i < k):
            bw_map[blocks[i]] = bw_map.get(blocks[i], 0) + 1
            i+=1
        min_w_count = bw_map['W']

        while(right < blocks_length):
            bw_map[blocks[right]] =  bw_map.get(blocks[right], 0) + 1
            bw_map[blocks[left]] -= 1
            left+=1
            min_w_count = min(min_w_count, bw_map.get('W', 0))
            right+=1
        return min_w_count

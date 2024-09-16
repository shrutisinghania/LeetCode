class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = defaultdict(int)
        for character in t:
            dict_t[character] += 1
        
        start_index = 0
        remaining_char = len(t)
        min_len = len(s)
        min_str = ''

        for index in range(len(s)):
            if s[index] in dict_t:
                dict_t[s[index]] -= 1
                if dict_t[s[index]] >= 0:
                    remaining_char -= 1

            if remaining_char == 0:
                while True:
                    if s[start_index] not in dict_t:
                        start_index += 1
                    elif dict_t[s[start_index]] != 0:
                        dict_t[s[start_index]] += 1
                        start_index += 1
                    else:
                        break

                if index - start_index < min_len:
                    min_str = s[start_index : index + 1]
                    min_len = index - start_index

                dict_t[s[start_index]] += 1
                start_index += 1
                remaining_char += 1

        return min_str
                

                


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for word in strs:
            sorted_word = "".join(sorted(word)) #here after sorting  it will give list of character.but we want as string so .join used

            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]

        return list(anagrams.values())


        # anagram_map = defaultdict(list)
        # for word in strs:
        #     count = [0] * 26

        #     for ch in word:
        #         count[ord(ch) - ord('a')] += 1

        #     key = tuple(count)
        #     anagram_map[key].append(word)

        # return list(anagram_map.values())    
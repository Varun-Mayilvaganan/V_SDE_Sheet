class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # why we use "set" :-
        # 1. comparison made simple using subset operator <=
        # 2. checking unique for reduced complexity
        row1, row2, row3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        valid_words = []
        for word in words:
            set_words = set(word.lower())
            if set_words <= row1 or set_words <= row2 or set_words <= row3:
                valid_words.append(word)
        return valid_words

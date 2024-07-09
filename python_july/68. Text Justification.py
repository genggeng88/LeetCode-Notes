class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def get_words(i):
            current_length = 0
            line = []
            while i < len(words) and len(words[i]) + current_length <= maxWidth:
                line.append(words[i])
                current_length += len(words[i]) + 1
                i += 1
            return line
        
        def create_line(line, i):
            base_length = -1
            for word in line:
                base_length += len(word) + 1
            
            extra_spaces = maxWidth - base_length

            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extra_spaces
            
            word_count = len(line) - 1
            spaces_per_word = extra_spaces // word_count
            needs_extra_space = extra_spaces % word_count

            for j in range(needs_extra_space):
                line[j] += " "
            
            for i in range(word_count):
                line[i] += " " * spaces_per_word
            
            return " ".join(line)



        i = 0
        ans = []

        while i < len(words):
            current_line = get_words(i)
            i += len(current_line)
            ans.append(create_line(current_line, i))
        
        return ans
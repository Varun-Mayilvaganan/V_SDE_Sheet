class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1  # Start with the first line
        current_width = 0  # Initialize the width of the current line
        
        for char in s:
            # Get the width of the current character
            char_width = widths[ord(char) - ord('a')]
            
            # If adding this character exceeds 100 pixels, we need a new line
            if current_width + char_width > 100:
                lines += 1  # Increment the line count
                current_width = char_width  # Start the new line with the current character
            else:
                current_width += char_width  # Add the character to the current line
        
        return [lines, current_width]

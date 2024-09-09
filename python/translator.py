import sys

# Define the Braille alphabet mapping
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", ".O.OOO": "1", ".O..OO": "2", ".O..O.": "3",
    ".O.O..": "4", ".O...O": "5", ".OO..O": "6", ".OO.O.": "7", ".O.O.O": "8",
    "..OO.O": "9", "..O.OO": "0"
}
# Inverse dictionary for English to Braille
english_to_braille = {v: k for k, v in braille_to_english.items()}

def translate(input_string):
    # Determine if input is Braille or English
    if set(input_string).issubset({'O', '.', ' '}):
        # Input is Braille, translate to English
        words = input_string.split(' ')
        english_translation = []
        for word in words:
            letters = [word[i:i+6] for i in range(0, len(word), 6)]
            translated_word = ''.join([braille_to_english.get(letter, '') for letter in letters])
            english_translation.append(translated_word)
        return ' '.join(english_translation)
    else:
        # Input is English, translate to Braille
        braille_translation = []
        for char in input_string:
            braille_translation.append(english_to_braille.get(char.lower(), ''))
        return ''.join(braille_translation)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)
    input_text = sys.argv[1]
    output_text = translate(input_text)
    print(output_text)


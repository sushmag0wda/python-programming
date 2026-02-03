# STRINGS IN PYTHON
'''
- A string is a collection of characters enclosed in quotes.
  - Can use single (' '), double (" "), or triple (''' ''' or """ """) quotes
  - Example: 'hello', "world",''' 
#'''multiline'''

'''- Strings are immutable:
  - Once created, you cannot change a character.
  - Example: s = "hello" → s[0] = 'H' # Not allowed

- Strings are indexed:
  - Each character has an index starting from 0
  - Negative indexing allowed (-1 is last character)
  - Example: s = "hello"
      s[0] = 'h'
      s[-1] = 'o'

- Strings are iterable:
  - Can loop through each character
  - Example: for ch in "hello": print(ch)

- Common operations:
  1. Length of string
     - len(s)
     - Example: len("hello") → 5
  2. Concatenation
     - s1 + s2
     - Example: "Hello" + "World" → "HelloWorld"
  3. Repetition
     - s * n
     - Example: "ha" * 3 → "hahaha"
  4. Membership test
     - 'a' in s / 'x' not in s
  5. Slicing
     - s[start:end:step]
     - Example: s = "hello"
        s[1:4] → "ell"
        s[::-1] → reverse string
  6. String methods
     - s.upper() → convert to uppercase
     - s.lower() → convert to lowercase
     - s.strip() → remove leading/trailing spaces
     - s.replace(old, new)
     - s.split(separator) → splits string into list
     - s.join(iterable) → joins elements into string
     - s.find(substr) / s.index(substr) → find index
     - s.count(substr) → count occurrences
     - s.startswith(sub) / s.endswith(sub)
  7. Formatting
     - f-strings: f"Hello {name}"
     - .format(): "Hello {}".format(name)
     - % formatting: "Hello %s" % name
  8. Escape sequences
     - \n → new line
     - \t → tab
     - \\ → backslash
     - \' → single quote
     - \" → double quote

- Strings can be converted to other types:
  - str(num) → string from number
  - int(s) → integer from string if numeric
  - float(s) → float from string if numeric

- Use Cases:
  - Storing text data
  - Processing user input
  - Formatting output
  - Parsing files
'''

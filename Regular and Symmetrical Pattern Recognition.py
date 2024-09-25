def detect_all_patterns(input_string):
  patterns = set()

  for i in range(len(input_string)):
      for j in range(i + 1, len(input_string) + 1):
          pattern = input_string[i:j]
          reverse_pattern = pattern[::-1]

          # This one is for symmetrical recognition
          if pattern == reverse_pattern and len(pattern) > 1:
              patterns.add(pattern)
          # And this one is for regular repetition
          if len(pattern) > 1 and input_string.count(pattern) > 1:
              patterns.add(pattern)

  # Exclude the input string itself
  patterns.discard(input_string)

  if patterns:
      print("Detected patterns:")
      for pattern in patterns:
          print(pattern)
  else:
      print("No patterns detected.")


def detect_longest_patterns(input_string):
  regular_patterns = set()
  symmetrical_patterns = set()

  for i in range(len(input_string)):
      for j in range(i + 1, len(input_string) + 1):
          pattern = input_string[i:j]

          # Regular repetition pattern
          if len(pattern) > 1 and input_string.count(pattern) > 1 and pattern != input_string:
              regular_patterns.add(pattern)

          # Symmetrical pattern
          if pattern == pattern[::-1] and len(pattern) > 1 and pattern != input_string:
              symmetrical_patterns.add(pattern)

  # Exclude the input string itself
  regular_patterns.discard(input_string)
  symmetrical_patterns.discard(input_string)

  if not regular_patterns and not symmetrical_patterns:
      return

  # Sort regular patterns by length in descending order
  sorted_regular_patterns = sorted(regular_patterns, key=len, reverse=True)
  longest_regular_length = len(sorted_regular_patterns[0]) if sorted_regular_patterns else 0

  # Sort symmetrical patterns by length in descending order
  sorted_symmetrical_patterns = sorted(symmetrical_patterns, key=len, reverse=True)
  longest_symmetrical_length = len(sorted_symmetrical_patterns[0]) if sorted_symmetrical_patterns else 0

  if regular_patterns:
    # Display all longest regular patterns
    print("\nThe list of detected longest regular repetition patterns:")
    for pattern in sorted_regular_patterns:
      if len(pattern) == longest_regular_length:
        print(pattern)

  if symmetrical_patterns:
  # Display all longest symmetrical patterns
    print("\nThe list of detected longest symmetrical patterns:")
    for pattern in sorted_symmetrical_patterns:
      if len(pattern) == longest_symmetrical_length:
        print(pattern)

def SimplePatternSuggest(string):
  suggested_characters = set()

  if len(string)>1:
    if len(string) %2==1:
      quotient, remainder=divmod(len(string),2)
      part1 = string[:quotient + remainder]
      part2 = string[quotient + remainder:]
      check= all(part1[index]==part2[index] for index in range(len(part1)-1))
      if check:
        suggested_characters.add(part1[len(part1)-1])

    for char in set(string):
      extended_string = string + char
      if extended_string == extended_string[::-1] and len(extended_string) > 1:
        suggested_characters.add(char)

  return suggested_characters
        

# Example usage:
input_str = input("Enter a string: ")
detect_all_patterns(input_str)
detect_longest_patterns(input_str)
print("\nThe next characters that could turn this string into a pattern: ")
print(SimplePatternSuggest(input_str))

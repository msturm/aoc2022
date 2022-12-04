# Open the file with the list of strings
with open('3.test') as f:
  # Read all the lines from the file
  lines = f.readlines()

# Initialize the total score to 0
score = 0

# Loop through each string in the file
for line in lines:
  # Strip whitespace from the line
  line = line.strip()

  # Split the line into two equal-length substrings
  s1, s2 = line[:len(line)//2], line[len(line)//2:]

  # Find the common character in the two substrings
  common_char = set(s1).intersection(s2).pop()

  # Convert the character to a number
  if common_char.islower():
    # Convert lowercase letters to numbers between 1 and 26
    num = ord(common_char) - ord('a') + 1
  elif common_char.isupper():
    # Convert uppercase letters to numbers between 27 and 53
    num = ord(common_char) - ord('A') + 27

  # Add the number to the total score
  score += num

# Print the total score
print(score)
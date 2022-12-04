# Open the file with the list of strings
with open('3.in') as f:
  # Read all the lines from the file
  lines = f.readlines()

# Initialize the total score to 0
score = 0

# Loop through each group of three strings
for i in range(0, len(lines), 3):
  # Get the current group of three strings
  s1, s2, s3 = lines[i:i+3]

  # Strip whitespace from the strings
  s1 = s1.strip()
  s2 = s2.strip()
  s3 = s3.strip()

  # Find the common characters in the three strings
  common_chars = set(s1).intersection(s2, s3)

  # Loop through each common character
  for c in common_chars:
    # Convert the character to a number
    if c.islower():
      # Convert lowercase letters to numbers between 1 and 26
      num = ord(c) - ord('a') + 1
    elif c.isupper():
      # Convert uppercase letters to numbers between 27 and 53
      num = ord(c) - ord('A') + 27

    # Add the number to the total score
    score += num

# Print the total score
print(score)
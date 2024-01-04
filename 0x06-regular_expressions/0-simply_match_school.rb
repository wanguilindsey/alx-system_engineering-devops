#!/usr/bin/env ruby

# Get the first command-line argument
string_to_match = ARGV[0]

# Define the regular expression using Oniguruma syntax
regex = /School/

# Check if the string matches the regular expression
if regex.match(string_to_match)
  # If there is a match, print the matched part of the string
  puts string_to_match.match(regex)[0] + "$"
else
  # If there is no match, print an empty line
  puts "$"
end

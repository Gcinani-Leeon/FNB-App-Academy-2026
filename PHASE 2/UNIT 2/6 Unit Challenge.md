# The Challenge

## “The Secure Password Hint Tool”

Users often forget their passwords. Create a script that helps them by showing a secure hint.
- Ask the user to input their secret password.
- Use .strip() to clean up any accidental spaces they might have typed at the start or end.
- Grab the very first letter and the very last letter of the password using string indexing.
- Print a hint using an f-string that forces the letters into uppercase so they stand out.

e.g: “Your password hint: It starts with P and ends with N”

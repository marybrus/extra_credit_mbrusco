# extra_credit_mbrusco
**What was the extra work**
The extra work here is that I created a program that can virtually find the union between any two strings. I also showed how we can exercise the libraries of python to help us in Theory of Computing. 

**Why did you choose it (i.e. in what area did you feel deficient and how did this work help improve your understanding) You can point to specific homeworks or problem types on exams.**

**What files are what?**
There is only one file, main.py which serves to allow a user to input a string, and tests to see whether that sting is in A U B. A = a*, B= b+. "re.compile()" compiles the regular expressions into objects for efficient matching. ^ ensures the match starts at the beginning of the string and $ ensures the match ends at the end of the string, both known as "anchors." * matches zero or more occurrences of 'a', and + matches one or more occurrences of 'B'. "pattern_a.match(input_string)" returns a match object if input_string matches the pattern for A, otherwise None. "pattern_b.match(input_string)" returns a match object if input_string matches the pattern for B, otherwise None. The condition checks if either pattern matches, returning True if the input is in the union of A and B, and False otherwise. the Program also prompts the user to enter a string. Calls is_in_union with the user’s input, then prints whether the input belongs to the union of A and B.


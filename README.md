# extra_credit_mbrusco
**What was the extra work**

The extra work here is that I created a program that can virtually find the union between any two strings. I also showed how we can exercise the libraries of python to help us in Theory of Computing. 



**Why did you choose it (i.e. in what area did you feel deficient and how did this work help improve your understanding) You can point to specific homework or problem types on exams.**

The choice to focus on this work was to strengthen my understanding of time complexity and to bridge the gap between theoretical computational models (like DTMs and NTMs) and their implementations in code. Time complexity is a foundational concept in computer science, but I often found myself struggling to analyze algorithms systematically to determine their time complexity, understand the implications of time complexity in the real world, and how to relate the theoretical bounds (like P vs. NP problems) to problems I encountered in homework and exams. This code snippet allowed me to experience analyzing the time complexity through the code of the machines we used in class. For example, we have been creating NTMS and DTMS practically all semester, but it is hard to see from a bunch of circles and arrows where the time complexity comes from. This project allowed me to translate what we have been doing in class into code which allowed me to see the time complexity in a more visually appealing way.



**What files are what?**

There is only one file, main.py which serves to allow a user to input a string, and tests to see whether that sting is in A U B. A = a*, B= b+. "re.compile()" compiles the regular expressions into objects for efficient matching. ^ ensures the match starts at the beginning of the string and $ ensures the match ends at the end of the string, both known as "anchors." * matches zero or more occurrences of 'a', and + matches one or more occurrences of 'B'. "pattern_a.match(input_string)" returns a match object if input_string matches the pattern for A, otherwise None. "pattern_b.match(input_string)" returns a match object if input_string matches the pattern for B, otherwise None. The condition checks if either pattern matches, returning True if the input is in the union of A and B, and False otherwise. the Program also prompts the user to enter a string. Calls is_in_union with the user’s input, then prints whether the input belongs to the union of A and B.


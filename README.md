# Fortune Validity Checker

## Description
This is a quick and dirty exercise based on a challenge from a friend: can you add and subtract the lucky numbers from a fortune cookie to equal the number of characters in your fortune?

This uses a depth-first recursive algorithm that tests adding and subtracting each user-supplied number until it finds an answer or runs out of options.

To run this, execute the Python3 file and open a browser window that loads your local host at port 5002, e.g., http://127.0.0.1:5002.

## Future changes
I wrote this in my "free time" between working full-time and taking classes at Oregon State. The functions, fortunate_numbers1() and fortunate_numbers2() are nearly identical and could be refactored into a single function. I can also get rid of the global variables and include helpful comments.

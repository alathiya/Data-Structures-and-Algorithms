import stack

string = "I am genius"

reversed_string = ""

s = stack.Stack()

# solution 
for ch in string:
	s.push(ch)

while(not s.is_empty()):
	reversed_string = reversed_string + s.peek()	
	s.pop()

print(reversed_string)
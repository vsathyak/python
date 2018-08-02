#break statement inside a nested loop (loop inside another loop), break will terminate the innermost loop.
for val in "string":
    print("Inside for loop")
    if val == "t":
        print("since if condition is success going to exit from entire loop")
        break
    print(val)
print("Exited from for loop")

# continue statement is used to skip the rest of the code inside a loop for the current iteration only.
for val in "string":
    if val == "i":
        print("Since if statement gt success skipping print and going back to for loop")
        continue
    print(val)
print("The end")

#we have a loop or a function that is not implemented yet, but we want to implement it in the future. But the body cannot be empty
#So, we use the pass statement to construct a body that does nothing.
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass
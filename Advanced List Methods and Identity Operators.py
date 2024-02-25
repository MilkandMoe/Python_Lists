#Task1:
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted_assignments = submitted.index((0),(1),(2),(3))
attended_last_class = attended.index((0),(1),(2))

#Tasks2:

if submitted == attended:
    print("The two list are identical in terms of their content, regardless of order.")


#Tasks3:

did_not_submit_assignments = attended.remove((1),(3))



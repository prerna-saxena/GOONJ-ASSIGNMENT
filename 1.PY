import ast

def flatten_and_filter(lst):
result = []
for item in lst:
if isinstance(item, list):
result.extend(flatten_and_filter(item))
elif item is not None and item != '':
result.append(item)
return result

def get_nested_list():
while True:
try:
user_input = input("Enter a nested list or type 'quit' to exit: ").strip()
if user_input.lower() == 'quit':
print("Exiting...")
exit()
nested_list = ast.literal_eval(user_input)

if isinstance(nested_list, list):
if any(isinstance(i, list) for i in nested_list):
return nested_list
else:
print("The list is not nested. Please enter a nested list.")
else:
print("Invalid input. Please enter a valid nested list.")
except (ValueError, SyntaxError):
print("Invalid input. Please enter a valid nested list.")

def main():
nested_list = get_nested_list()
flattened_list = flatten_and_filter(nested_list)
print("Flattened and filtered list:", flattened_list)

if __name__ == "__main__":
main()

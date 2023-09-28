import re

def arithmetic_arranger(problems, solve = False):
  """Arranges a list of arithmetic problems vertically and side-by-side.

  Args:
    problems: A list of strings, each representing an arithmetic problem.
    solve: A boolean value indicating whether to solve the problems.

  Returns:
    A string containing the problems arranged vertically and side-by-side, or an
    error message if the problems are not properly formatted.
  """

  if len(problems) > 5:
    return "Error: too many problems"

  arranged_problems = []

  for problem in problems:
    # Check for invalid characters in the problem.
    if re.match(r"[^\s0-9.+-]", problem):
      if re.search(r"[/]", problem) or re.search(r"[*]", problem):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    # Convert the first and second numbers to integers.
    first_number = int(problem.split(" ")[0])
    second_number = int(problem.split(" ")[2])

    # Check the length of the numbers.
    if len(str(first_number)) >= 5 or len(str(second_number)) >= 5:
      return "Error: Number can not be more than four digits."

    # Perform the arithmetic operation.
    sum = ""
    if operator == "+":
      sum = str(first_number + second_number)
    elif operator == "-":
      sum = str(first_number - second_number)

    # Format the output string.
    length = max(len(str(first_number)), len(str(second_number)))
    arranged_problems.append(f"{first_number:>{length}} {operator} {second_number:>{length-1}}")
    arranged_problems.append(f"{'-'*length:>{length}}")
    if solve:
      arranged_problems.append(f"{sum:>{length}}")

  # Remove any leading whitespace from the output string.
  arranged_problems = [string.lstrip() for string in arranged_problems]

  # Join the output lines into a string.
  arranged_problems_string = "\n".join(arranged_problems)

  return arranged_problems_string

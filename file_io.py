
# Create a python file in python, that itself modifies the testing.txt file
# to say I'm sorry, I cannot do that.

py_script = """
new_file = open("./file_io_hub/sorry_dave.txt", "w")
new_file.write("I'm sorry, I can't do that DAVE!")
new_file.close()
"""

new_file = open("./file_io_hub/testing.py", "w")
new_file.write(py_script)
new_file.close()

import file_io_hub.testing  # - import brings in code AND executes it!

###########################

# python_file = open("./file_io_hub/change_text.py", "w")
# valid_code = """
# to_change = open("./testing.txt", "w")
# to_change.write("I'm sorry Dave!")
# to_change.close()
# """
# python_file.write(valid_code)
# python_file.close()

# import file_io_hub.testing

################################

with open("with_statement.py", "w") as f:
    f.write("# - I'm a comment\nprint('Hello world')")



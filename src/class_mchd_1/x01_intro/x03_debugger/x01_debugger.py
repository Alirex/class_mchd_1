# %%
# You can use "debugger" to get more info about program, while develop it.

# Debugging is the process of detecting and removing of existing and potential errors (also called as 'bugs').

# You can add "breakpoint".
# For this, you can click to the left of the line.
#   Or, use the hotkey "Ctrl+F8".
my_variable = "Hi"

# With breakpoint and debugger program paused BEFORE breakpoint.

# !!! Place a breakpoint at the next line.

next_variable = "Hello"

print(my_variable)

# Make "Right mouse Click" at this script. And select "Debug ..." (with green bug).

# Now you in "Debugger".
# At this place, you can see your variables and their values.
#   Also, you can see some extra data.
#   For example - "type".
#   Or the inner structure of a variable.

# Controls:
#   - Rerun the script by "Ctrl+F5". Or by "rounded green arrow"
#   - Resume execution and go to the next "breakpoint" (or error) by "F9". Or by "green triangle".
#   - Step over code (Line by line) by "F8". Or by "blue arrow at right angles over white stripe"
#   - Stop execution by "Ctrl+F2". Or by "red square".
# Test other controls if you wish.

# You have the tab "Debugger". And tab "Console".
#   In "Console" you can see the output of your program and make interaction with it. As in normal execution.

# You can have a few active debuggers if you need.

# Thanks to the debugger, you can better understand what's going on in your program.
#   It is a great tool to help you with your research and learning.

# If this available, better to use the debugger for debugging.
# Do not use "print" for debugging if you can. Use "print" only for "output" for end-user.
# If you need print-like debug, `logging` can be more useful.

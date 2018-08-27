# Step 1:

Identity class functions that are not camel_case.

    $ rm camelcase_fns.txt
    $ python3 lib3to3.py /home/src/core9/Jumpscale/

# Step 2:

Run a comprehensive *NON-INTERACTIVE* "trace" on js_shell (or other program):

    $ python3 -m 'trace' js_shell 'j.tools.timer.test()' > trace_output.txt


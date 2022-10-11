## Shell variables expansions

Bash scripting involving variable declaration, shell expansions and more.

---

0. (\<o>) Create a script that creates an alias.

- Name <mark>`ls`</mark>
- Value: <mark>`rm *`</mark>
  > **Solution**
  >
  > _file_ `./0-alias` (executable)
  >
  > ```
  > #!/bin/bash
  > alias ls="rm *"
  > ```
  >
  > 2 lines

---

1. (Hello you) Create a script that prints <mark>`hello user`</mark>, where user is the current Linux user.
   > **Solution**
   >
   > _file_ `./1-hello_you` (executable)
   >
   > ```
   > #!/bin/bash
   > echo "hello $USER"
   > ```
   >
   > 2 lines

---

2. (The path to success is to take massive, determined action) Add <mark>`/action`</mark> to the PATH. <mark>`/action`</mark> should be the last directory the shell looks into when looking for a program.
   > **Solution**
   >
   > _file_ `./2-path` (executable)
   >
   > ```
   > #!/bin/bash
   > export PATH="$PATH:/action"
   > ```
   >
   > 2 lines

---

3. (If the path be beautiful, let us not ask where it leads) Create a script that counts the number of directories in the <mark>`PATH`</mark>
   > **Solution**
   >
   > _file_ `./3-paths` (executable)
   >
   > ```
   > #!/bin/bash
   > echo $PATH | tr : "\n" | wc -l
   > ```
   >
   > 2 lines

---

4. (Global variables) Create a script that lists environment variables.
   > **Solution**
   >
   > _file_ `./4-global_variables` (executable)
   >
   > ```
   > #!/bin/bash
   > printenv
   > ```
   >
   > 2 lines

---

5. (Local variables) Create a script that lists all local variables and environment variables, and functions.
   > **Solution**
   >
   > _file_ `./5-local_variables` (executable)
   >
   > ```
   > #!/bin/bash
   > set
   > ```
   >
   > 2 lines

---

6. (Local variable) Create a script that creates a new local variable.

- Name: <mark>BEST</mark>
- Value: <mark>School</mark>
  > **Solution**
  >
  > _file_ `./6-create_local_variable` (executable)
  >
  > ```
  > #!/bin/bash
  > BEST=School
  > ```
  >
  > 2 lines

---

7. (Global variable) Create a script that creates a new global variable.

- Name: <mark>BEST</mark>
- Value: <mark>School</mark>
  > **Solution**
  >
  > _file_ `./7-create_global_variable` (executable)
  >
  > ```
  > #!/bin/bash
  > export BEST=School
  > ```
  >
  > 2 lines

---

8. (Every addition to true knowledge is an addition to human power) Write a script that prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line.
   > **Solution**
   >
   > _file_ `./7-create_global_variable` (executable)
   >
   > ```
   > #!/bin/bash
   > export BEST=School
   > ```
   >
   > 2 lines

---

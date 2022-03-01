# Defang-IP
To convert an IP address to a defanged IP address, we need to replace “.” with “[.]”. During coding interviews, a standard problem for changing an IP address is that you receive a valid IP address, you must return a defanged version of that IP address.<br>
This is generally a warm-up question for coding interviews. Solving this question quickly will give a good impression that you know how to understand a problem statement quickly because there is not much that you need to solve this problem. You just need to replace every “.” with “[.]”.<br>
Now let’s see how to write a program to defang an Ip address using Python. Here you simply need to treat “.” as a separator and split the string. Then you have to rejoin an empty string and select “[.]” as the new separator.

anicli
=========

Animations for use on the command line in Python. If ever you wanted to make mundane tasks on the command line a bit more enjoyable, then you've found the right repo!

1. Progress bars
2. Pre/Post display of ReadMe or help options

Use:
####

You can use eithe ra list or a .ani file

````
import anicli

anicli.animate('happy.ani',0.5) # ani file, how long to display each frame per second (frame rate) 

# Or

happy = ['._.','^_^','._.']
anicli.animate(happy,0.5)
````

.Ani files
####

An animations is loaded via an **.ani** file. Many **.ani** files are stored in the **ani_files** folder. After spexifying the dimension of your animation, the divider is a simple *****. For example, this is 3 frames of a 1x3 animation:

._.
*****
^_^
*****
._.
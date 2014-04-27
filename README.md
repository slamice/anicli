anicli
=========

Animations for use on the command line in Python. If ever you wanted to make mundane tasks on the command line a bit more enjoyable, then you've found the right repo! These are perfect for:

1. Progress bars
2. Pre/Post display of ReadMe or help options
3. Command line email (one day?!)

### Use:

You can use either an .ani or a list to animate. e.g.:

````
import anicli

anicli.animate('happy.ani',0.5) # ani file, how long to display each frame per second (frame rate) 

# Or

happy = ['._.','^_^','._.']
anicli.animate(happy,0.5)
````

### .Ani files:

An animations is loaded via an __.ani__ file. Many __.ani__ files are stored in the __ani_files__ folder. The divider between frames is a simple *******. For example, these are 3 frames of a 1x3 animation:
````
._.
*******
^_^
*******
._.
````
### To come:
- Actual implemenation
- Color

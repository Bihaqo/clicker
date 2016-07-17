A simple program to label a computer vision dataset. To start it run
```
python clicker.py data/path
```

It shows you an image from `data/path`, you click on it, the program records the click position and shows you the next image.
After each click it updates the log file `coordinates.pickle`.

* You can close the program at any moment. On the next run you will start exactly where you finished, no data lost.
* You can click with left, right, or middle button of the mouse. Either way the program records the position of the click and the button used. So you can e.g. click suspicious images with the right button and then return to them later.

An example contents of the `coordinates.pickle` file:
```
{'data/1.jpg': {'y': 236, 'x': 429, 'button': 1, 'ydata': 203.6, 'xdata': 304.7}, 'data/2.jpg': {'y': 199, 'x': 242, 'button': 3, 'ydata': 242.2, 'xdata': 109.9}}
```

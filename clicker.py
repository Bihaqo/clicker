import matplotlib.pylab as plt
import os
import sys
import cPickle as pickle

path_to_pickle = 'coordinates.pickle'


class Clicker:
    def __init__(self, path):
        self.path = path
        if os.path.isfile(path_to_pickle):
            self.done = pickle.load(open(path_to_pickle, 'rb'))
            print(self.done)
        else:
            self.done = {}
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.files = [os.path.join(self.path, im) for im in os.listdir(path)]
        self.im_generator = self.get_im_generator()
        self.draw_next()
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        plt.show()


    def onclick(self, event):
        self.done[self.curr_image] = {'button': event.button, 'x': event.x,
                                      'y': event.y, 'xdata': event.xdata,
                                      'ydata': event.ydata}
        print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))
        pickle.dump(self.done, open(path_to_pickle, 'wb'))

        self.draw_next()


    def get_im_generator(self):
        for idx, im in enumerate(self.files):
            if im in self.done:
                continue
            yield idx, im

    def draw_next(self):
        try:
            self.curr_idx, self.curr_image = self.im_generator.next()
        except StopIteration:
            plt.close()
            return
        plt.title('%s, %d / %d' % (self.path, self.curr_idx + 1, len(self.files)))
        self.ax.imshow(plt.imread(self.curr_image))
        self.fig.canvas.draw()

if __name__ == "__main__":
    ob = Clicker(sys.argv[1])

from Queue import Queue
from threading import Thread
import sys
import svn.remote

class Worker(Thread):
    """Thread executing tasks from a given tasks queue"""
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception, e:
                print e
            finally:
                self.tasks.task_done()

class ThreadPool:
    """Pool of threads consuming tasks from a queue"""
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads): Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()

def dump(plugin_base, repo_path):
    plugin_repo = plugin_base + repo_path
    print "{+} Now grabbing %s" %(plugin_repo)
    try:
        print "{+} Now grabbing %s" %(plugin_repo)
        s = svn.remote.RemoteClient(plugin_repo)
        s.checkout("./%s" %(repo_path))
    except Exception, e:
        print e

def main(args):
    if len(args) != 2:
        sys.exit("use: %s http://svn.org.com/" %(args[0]))
    r = svn.remote.RemoteClient(args[1])
    pool = ThreadPool(40)
    for repo_path in r.list():
        pool.add_task(dump, args[1], repo_path)
    pool.wait_completion()
    print "done..."

if __name__ == '__main__':
    main(args=sys.argv)

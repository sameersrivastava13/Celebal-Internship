import threading


class MyProgram(threading.Thread):
    def __init__(self, name, thread_no):
        threading.Thread.__init__(self)
        self.name = name
        self.thread_no = thread_no

    def run(self):
        print("Starting Thread ", self.name)
        print("Exiting Thread ", self.thread_no)


if __name__ == "__main__":
    thread_1 = MyProgram("sameer", 1)
    thread_2 = MyProgram("Celebal", 2)

    # starting the threads
    thread_1.start()
    thread_2.start()

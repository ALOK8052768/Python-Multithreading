from multiprocessing import Process, Queue

def worker(q):
    message = q.get()
    print("Received:", message)

if __name__ == "__main__":

    q = Queue()

    p = Process(target=worker, args=(q,))

    p.start()

    q.put("Hello Process")

    p.join()
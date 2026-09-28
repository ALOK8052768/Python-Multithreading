import multiprocessing
def test():
    print("My name is Alok pariyar")

if __name__=="__main__":
    p=multiprocessing.Process(target=test)

    p.start()
    p.join()

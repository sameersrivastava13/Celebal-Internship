import multiprocessing


def Company_name(name):
    print("Name of the company:\t", name)


def Designation(name):
    print("Designation in the company:\t", name)


if __name__ == "__main__":
    arr = ["Celebal Technologies", "Python Developer"]

    process_1 = multiprocessing.Process(target=Company_name, args=(arr[0],))
    process_2 = multiprocessing.Process(target=Designation, args=(arr[1]
                                                                  ,))

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

    print("End of Program")

import numpy as np

K = 6
def colapse_table(data):

    W1 = np.array(
        [
        [1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1]
        ]
    )

    W2 = np.array(
        [
        [1, 1, 0],
        [0, 0, 1]
        ]
    )


    return [W2.dot(W1.dot(x).dot(W1.T)).dot(W2.T) for x in data]

    
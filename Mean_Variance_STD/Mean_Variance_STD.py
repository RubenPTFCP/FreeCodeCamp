import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(numbers).reshape(3, 3)
    stats = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    funcs = [np.mean, np.var, np.std, np.max, np.min, np.sum]

    return {
        name: [f(arr, axis=0).tolist(), f(arr, axis=1).tolist(), f(arr).item()]
        for name, f in zip(stats, funcs)
    }


print(calculate([0,1,2,3,4,5,6,7,8]))





import numpy as np
import pandas as pd


def get0to100():
    return np.random.randint(0, 101)


if __name__ == "__main__":
    # feature = np.arange(6,21)
    # label = feature * 3 + 4
    # print("特征:", feature)
    # print("标签:", label)
    # noise = np.random.random((15,)) + np.random.randint(low=-2,high=2,size=(15,))
    # label = noise + label
    # print(label)
    col_name = ["Eleanor", "Chidi", "Tahani", "jason"]
    my_data = np.random.randint(low=0, high=101, size=(3, 4))
    pd_data = pd.DataFrame(data=my_data, columns=col_name)
    print(pd_data)
    print(pd_data[0:1])
    el = pd_data["Eleanor"]
    print(el)
    pd_data["Janet"] = pd_data["Tahani"] + pd_data["jason"]
    print(pd_data)
    pd_data = pd_data.set_index('Eleanor')
    print(pd_data)
    new_pd = pd_data["Chidi"]
    print(new_pd)

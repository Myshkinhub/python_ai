import numpy as np


def create_array():
    arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype='int32')
    print(f"arr1: {arr1}")
    print(f"arr1.ndim: {arr1.ndim}")
    print(f"arr1.shape: {arr1.shape}")
    print(f"arr1.dtype: {arr1.dtype}")
    print(f"arr1.itemsize: {arr1.itemsize}")
    print(f"arr1.data: {arr1.data}")

    # 全 0 数组
    arr2 = np.zeros((2, 3))
    print(f"arr2: {arr2}")

    # 全 1 数组
    arr3 = np.ones((2, 3))
    print(f"arr3: {arr3}")

    # 填充数组
    arr3 = np.full((2,3),5,dtype="int64")

    np.random.seed(19)
    # 均匀分布数组（0，1）
    arr4 = np.random.rand(10)
    print(f"arr4: {arr4}")

    # 正态分布数组
    arr5 = np.random.randn(10)
    print(f"arr5: {arr5}")

    # 随机整数数组(左闭右开)
    arr6 = np.random.randint(0,9, (3,3))
    print(f"arr6: {arr6}")

    # 单位数组
    arr7 = np.eye(3,3)
    print(f"arr7: {arr7}")

    # 线性数组
    arr8 = np.linspace(0,10,10,endpoint=False)
    print(f"arr8: {arr8}")

def slice_array():
    arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(arr)

    # 获取第0维，第一个元素
    print(arr[0,1])

    # 获取第0维第一个和第1维第一个元素
    print(arr[0:2,1])

    # 获取所有行，第0列的元素
    print(arr[:,0])

    # 布尔索引
    mask = arr > 5
    print(mask)
    print(arr[mask])

    # 花式索引

    print(arr[[0,2],[1,0]])

# 广播机制
def broad_cast():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    # 逐个元素计算
    print(f'a + b: {a + b}')
    print(f'a * b: {a * b}')
    print(f'a / b: {a / b}')
    print(f'a // b: {a // b}')
    print(f'a - b: {a - b}')
    print(f'a ** 2: {a ** 2}')

    # 一维时，@相当于求内积
    print(f'a @ b: {a @ b}')

    c = np.array([[1,2,3],[4,5,6]])
    d = np.array([[1,2,3],[4,5,6]])

    d2 = d.reshape(3,2)
    print(f'c @ d2:{c @ d2}')


    array1 = np.array([[1,2,3],[4,5,6]])
    array2 = np.array([7,8,9])

    print(array1 + array2)



def reshape_array():
    arr = np.arange(6)
    print(arr)

    arr1 = arr.reshape((2,3))
    print(arr1)

    # 返回副本
    arr2 = arr1.flatten()
    arr2[0]=99
    print(arr2)

    # 尽量返回视图
    arr3 = arr1.ravel()
    print(arr3)

    # 两种转置方式均返回视图
    arr4 = arr1.T
    print(arr4)

    # transpose 对于高维数组可以指定各个维度怎么转换
    arr5 = arr4.transpose()
    print(arr5)

    # 拼接
    # 拼接时两个数组维度要相同，除了拼接轴外，其他维度的形状要一致
    a = np.array([[1,2],[3,4]])
    b = np.array([[5,6]])

    # 按行拼接，第0维
    e = np.concatenate((a,b),axis=0)
    print(f'e: {e}')


    # 按列拼接，第1维
    f = np.concatenate((a,b.T),axis = 1)
    print(f'f: {f}')

    # 展平后拼接
    g = np.concatenate((a,b),axis = None)
    print(f'g: {g}')

    # 垂直堆叠
    h = np.vstack((a,b))
    print(f'h: {h}')

    # 水平堆叠
    i = np.hstack((a,b.T))
    print(f'i: {i}')

    # 拼接是底层基础操作，堆叠是封装好的快捷方式
    # 堆叠的要求相对宽容，比如 vstack 能把一维数组自动升维成二维再拼
    # 日常编码尽量使用堆叠，可读性较高

def math_array():
    arr = np.array([[1,2],[3,4]])
    # 求和
    # 按照行求和，第0维
    print(np.sum(arr,axis = 0))

    # 按照列求和，第1维
    print(np.sum(arr,axis = 1))

    # 所有元素求和
    print(np.sum(arr,axis = None))

    # 求均值
    # 第0维，按照行求均值
    print(np.mean(arr, axis = 0))

    # 第1维，按照列求均值
    print(np.mean(arr, axis = 1))

    # 所有元素求均值
    print(np.mean(arr, axis=None))

    print(f'std: {np.std(arr)}')
    print(f'var: {np.var(arr)}')
    print(f'max: {np.max(arr)}')
    print(f'argmax: {np.argmax(arr)}')


def save_load():
    arr = np.array([[1,2],[3,4],[5,6]])
    np.save("filedata/data.npy",arr)

    arr_load = np.load("filedata/isic_test_masks.npy",'r')
    print(arr_load)

    # csv文本
    np.savetxt("filedata/text.csv",arr,delimiter=',')
    arr_text = np.loadtxt("filedata/text.csv",delimiter=',')
    print(arr_text)

if __name__  == "__main__":
    reshape_array()



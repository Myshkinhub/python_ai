import numpy as np

# 1.模拟数据
np.random.seed(10)
feature_data = np.random.randn(200,3)*5 +10
print(f'feature_data:\n{feature_data}')

# 2.数据标准化处理
mean = np.mean(feature_data,axis = 0)
std = np.std(feature_data, axis = 0)
print(f'mean:\n{mean}')
print(f'std:\n{std}')

norm_data = (feature_data - mean) / std
print(f'norm_data:\n{norm_data}')
print(f'norm_data shape:\n{norm_data.shape}')

print(f'标准化后均值:\n{np.mean(norm_data,axis = 0)}')
print(f'标准化后标准差:\n{np.round(np.std(norm_data,axis = 0),2)}')

# 3.用3σ原则筛选异常值
outlier_mask = abs(norm_data) > 3
print(f'outlier_mask:\n{outlier_mask}')
outlier_count = np.sum(outlier_mask)
print(f'异常值个数: {outlier_count}')

# 4.剔除含有异常值的样本
row_outlier_mask = ~np.any(outlier_mask, axis = 1)
print(row_outlier_mask)

# 用 norm_data 找出异常值，feature_data是原始数据
clean_data = feature_data[row_outlier_mask]
print(f'原始样本数: {norm_data.shape[0]}\n清洗后的样本数: {clean_data.shape[0]}')

# 5. 输出清洗后数据统计信息
print("\n清洗后数据统计：")
print(f"均值：{np.round(np.mean(clean_data, axis=0), 2)}")
print(f"最大值：{np.round(np.max(clean_data, axis=0), 2)}")
print(f"最小值：{np.round(np.min(clean_data, axis=0), 2)}")
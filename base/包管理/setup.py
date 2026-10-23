from setuptools import setup, find_packages

setup(
    name='datatools',
    version='1.0.0',
    description='数据处理工具包',
    author='Your Name',
    author_email='3198353401@qq.com',
    url='https://github.com/Myshkinhub/python_ai/tree/main/base/datatools',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'numpy>=1.19.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
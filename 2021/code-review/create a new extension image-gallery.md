[PR](https://github.com/Azure/azure-cli-extensions/pull/4050/files)
[document](https://docs.microsoft.com/en-us/azure/virtual-machines/shared-image-galleries)
gallery: 可以分享你保存image, image definition, image version的镜像仓库, 类似 docker image repository

__all__，其他文件中使用from xxx import *导入该文件时，只会导入 __all__ 列出的成员，可以其他成员都被排除在外。
-universal的意思是这个二进制包对所有 支持的 Python 版本和 ABI 都适用，「 一处打包，到处使用」，生成的文件名类似：my_package-0.1.0-py3-none-any.whl

__import__('pkg_resources').declare_namespace(__name__)
如果这里代码是 my_namespace/__init__.py，那么 __name__ 是 my_namespace
foo = __import__('bar') 
此时__name__ 是bar
命名空间包： 将软件产品拆分为多个部分，并作为可选插件发布。
"""
scooby是一个轻量级的工具，用于轻松报告 Python 环境的包版本和硬件资源。
"""
import scooby

# 报告 Python 环境最基础的包版本(numpy scipy IPython matplotlib scooby)以及硬件资源
print(scooby.Report())

# 自定义添加还想要报告的包 (如果无法导入包或无法确定包的版本，scooby也会报告)
report = scooby.Report(additional=['pyvista', 'vtk', 'no_version', 'does_not_exist'])
print(report)


# 获得任意一个包的版本
import numpy
print(scooby.get_version(numpy))


# 自定义一个Report
class Report(scooby.Report):
    def __init__(self, additional=None, ncol=3, text_width=80, sort=False):
        """Initiate a scooby.Report instance."""

        # Mandatory packages.
        core = ['pyvista', 'stDrosophila', 'numpy', 'scooby']

        # Optional packages.
        optional = ['vtk', 'pandas', 'matplotlib']

        scooby.Report.__init__(self, additional=additional, core=core,
                               optional=optional, ncol=ncol,
                               text_width=text_width, sort=sort)

print(Report())


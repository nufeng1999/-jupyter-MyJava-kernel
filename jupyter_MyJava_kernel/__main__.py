from ipykernel.kernelapp import IPKernelApp
from .kernel import JavaKernel
IPKernelApp.launch_instance(kernel_class=JavaKernel)

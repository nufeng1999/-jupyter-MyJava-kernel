from setuptools import setup

setup(name='jupyter_MyJava_kernel',
      version='0.0.1',
      description='Minimalistic Java kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyJava-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyJava-kernel/tarball/0.0.1',
      packages=['jupyter_MyJava_kernel'],
      scripts=['jupyter_MyJava_kernel/install_MyJava_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'java'],
      include_package_data=True
      )

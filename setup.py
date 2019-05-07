from setuptools import setup

setup(name='pytorch_vgg_named',
      version='0.1',
      description='Provides a version of the popular VGG networks that can be used as feature extractors similar to how to query nodes in tensorflow. Mostly useful for style transfer code.',
      url='http://github.com/black-puppydog/pytorch_vgg_named',
      author='Daan Wynen',
      author_email='daan.wynen@inria.fr',
      packages=['vgg_named'],
      zip_safe=False)

from setuptools import setup
import requests

url = 'https://github.com/foamliu/Deep-Image-Matting-PyTorch/releases/download/v1.0/BEST_checkpoint.tar'
r = requests.get(url)
with open('BEST_checkpoint.tar', mode='w+b') as f:
    f.write(r.content)

setup(
    name="deep_image_matting",
    version="1.0",
)

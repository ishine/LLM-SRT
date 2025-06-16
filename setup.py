from setuptools import setup

setup(
    name="slam-llm",
    version="0.0.1",
    packages=["src/slam_llm"],  # 与 Hatch 配置一致
    install_requires=open("requirements.txt").read().splitlines(),
)
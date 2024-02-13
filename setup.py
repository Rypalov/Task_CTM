import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

    name='Rypalov_task_CTM',
    version='0.2',
    author="Rypalov Aleksandr",
    author_email="@Rypalov_Aleksandr",
    description="Упакованный проект для установки",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rypalov/Task_CTM",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
    ],
)
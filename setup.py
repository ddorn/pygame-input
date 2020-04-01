from setuptools import setup


with open("pygame_input.py") as f:
    info = {}
    for line in f.readlines():
        if line.startswith("__version__"):
            exec(line, info)
            break

README = open("readme.md").read()

setup(
    name="pygame-input",
    version=info["__version__"],
    author="Diego Dorn",
    author_email="pygame-input@lama-corp.space",
    description="pygame-input is a tool to simplify input handling with pygame",
    long_description=README,
    license="MIT",
    keywords="pygame,game,input,joystick",
    url="https://gitlab.com/ddorn/pygame-input",
    download_url="https://gitlab.com/ddorn/pygame-input/releases",
    platforms="POSIX, Windows, MacOS X",
    py_modules=["pygame_input"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries"
        "Topic :: Software Development :: Libraries :: pygame",
    ],
)

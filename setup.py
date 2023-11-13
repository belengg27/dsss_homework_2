from setuptools import setup, find_packages

setup(
    name='math-quiz',
    version='0.1.0',
    description='Homework 2 in course Data Science Survival Skills',
    url='https://github.com/belengg27/dsss_homework_2',
    author='Belen Gomez Garcia',
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'math-quiz = math_quiz.math_quiz:main',
        ],
    },
)

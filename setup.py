import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='crystpredict',
    version='0.0.31',
    author='Dunce Caps',
    author_email='pykachu6@uw.edu',
    description='Crystal predictor',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/pykachu6/Dunce-Caps',
    license='MIT',
    packages=['toolbox'],
)
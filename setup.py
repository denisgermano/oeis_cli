from setuptools import setup

setup(
    name="oeis_query",
    version="0.1",
    python_requires='>=3.5',
    py_modules=["oeis_query"],
    install_requires=["click", "lxml", "requests"],
    entry_points="""
        [console_scripts]
        oeis_query=oeis_query:cli
    """,
)

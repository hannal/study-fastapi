python_sources(
    name="proj",
    sources=["*.py", "**/*.py", "!**/test_*.py", "!tests"],
    dependencies=[
        "//:reqs",
    ],
)

python_requirements(
    name="reqs",
    source="requirements.txt",
)

poetry_requirements(name="poetry", source="pyproject.toml")

python_tests(
    name="tests",
    sources=[
        "**/test_*.py",
    ],
)
pex_binary(
    name="pex_binary",
    dependencies=[
        ":proj",
    ],
    entry_point="main.py",
)

resource(name="pyproject", source="pyproject.toml")

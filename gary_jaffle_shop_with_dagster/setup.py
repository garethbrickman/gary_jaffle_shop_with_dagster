from setuptools import find_packages, setup

setup(
    name="gary_jaffle_shop_with_dagster",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "gary_jaffle_shop_with_dagster": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-duckdb<1.10",
        "cowsay"
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)


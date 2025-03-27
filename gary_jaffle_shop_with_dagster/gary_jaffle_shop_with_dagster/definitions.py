from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import jaffle_shop_dbt_assets, haverview_ddl
from .project import jaffle_shop_project
from .schedules import schedules

defs = Definitions(
    assets=[jaffle_shop_dbt_assets, haverview_ddl],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=jaffle_shop_project),
    },
)

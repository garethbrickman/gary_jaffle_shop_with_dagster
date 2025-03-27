from dagster import AssetExecutionContext, asset
from dagster_dbt import DbtCliResource, dbt_assets
import json

from .project import jaffle_shop_project


@dbt_assets(manifest=jaffle_shop_project.manifest_path)
def jaffle_shop_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

@asset
def haverview_ddl(context: AssetExecutionContext, dbt: DbtCliResource) -> None:
    dbt.cli(
        ["--cache-selected-only", "run-operation", "customers", "--args", json.dumps(context.op_config)],
        context=context,
        manifest=jaffle_shop_project.manifest_path,
    ).wait()
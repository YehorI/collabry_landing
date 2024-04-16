import asyncio
import typer


def run(ctx: typer.Context):
    loop: asyncio.AbstractEventLoop = ctx.obj["loop"]
    settings: Settings = ctx.obj["settings"]
    
    service = get_service(loop=loop, settings=settings)

    loop.run_until_complete(service.run())


def get_cli() -> typer.Typer:

    cli = typer.Typer()

    cli.command(name="run")(run)
    ...

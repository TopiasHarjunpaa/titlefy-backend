from invoke import task

@task
def start(ctx):
    ctx.run("export FLASK_APP=src.app && flask run", pty=True)
import subprocess


def activate():
    subprocess.run(["$(poetry env info --executable)"], executable="/bin/bash")


def make_migrations():
    message = input("Enter migration message: ")
    subprocess.run(
        f"cd $(git rev-parse --show-toplevel)/src && alembic revision --autogenerate -m '{message}'",
        shell=True,
    )


def migrate():
    subprocess.run("cd $(git rev-parse --show-toplevel)/src && alembic upgrade head", shell=True)
    print("Migrations complete!")


def local_server():
    subprocess.run("cd $(git rev-parse --show-toplevel) && docker-compose up -d", shell=True)


def lint():
    subprocess.run("cd $(git rev-parse --show-toplevel) && black src", shell=True)


def test():
    subprocess.run("cd $(git rev-parse --show-toplevel)/src && pytest", shell=True)

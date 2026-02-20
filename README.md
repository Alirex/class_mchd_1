# Classwork for MCHD-1

---

# 🛠️ Development

## Uv install or update

https://docs.astral.sh/uv/getting-started/installation/

```bash
if ! command -v uv &> /dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh;
else
    uv self update;
fi

uv --version
```

## Create venv

```bash
uv sync
```

or, if you need more:

```bash
uv sync --all-packages --all-groups --all-extras
```

## Register pre-commit hooks

Make this after cloning the repository.

```shell
prek install
```

or, if you have pre-commit hooks installed before prek:

```shell
prek install --overwrite
```

Make this each time after cloning the repository.

Don't need to do it after changing the hooks, commit or pull.

## Run pre-commit hooks

If needed, run them manually.

```shell
prek run --all-files
```

Useful after changing the hooks. Or just to check if everything is fine.

## Update dependencies

You can use this tool:

- [uv-upgrade](https://github.com/Alirex/uv_upgrade)

After installing it, run:

```shell
uv-upgrade
```

---

# Extra

- Why is the `.idea` folder is partially stored in the repository?
  - [read (UKR)](https://github.com/Alirex/notes/blob/main/notes/ignore_or_not_ide_config/ukr.md)
- Why `py.typed`?
  - [mypy (ENG)](https://mypy.readthedocs.io/en/stable/installed_packages.html#creating-pep-561-compatible-packages)
  - [typing (ENG)](https://typing.python.org/en/latest/spec/distributing.html#packaging-type-information)

## Reinit .idea folder for git for better gitignore support

If you created a new project with JetBrains IDE and automatically created git repository,
before providing more granular `.gitignore` file, you need to reinit `.idea` folder.

```shell
git rm -r --force --cached .idea &&\
git add .idea
```

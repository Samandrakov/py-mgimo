import shlex
import shutil
import subprocess

import pytest


def run_command(cmdline: str) -> str:
    if shutil.which("uv") is None:
        pytest.skip("uv не установлен")
    args = shlex.split(cmdline)
    header = ["uv", "run", "mgimo"]
    proc = subprocess.run(header + args, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    return proc.stdout.strip()


def test_translate_random_parameter():
    out = run_command('translate "Hello, world!" --from en --to random')
    assert len(out) > 0, out


def assert_returns(cmdline: str, expected_output: str):
    out = run_command(cmdline)
    assert expected_output in out, out


def test_cli_translate_hello_text():
    assert_returns("translate Привет --from ru --to es", "Hola")


def test_cli_translate_detect():
    assert_returns('translate "это текст на русском" --detect', "ru")


def test_cli_translate_list():
    out = run_command("translate --list")
    assert "zu: zulu" in out


def test_provided_languages_search_bel():
    out = run_command("translate --list --contains bel")
    assert "be: belarusian" in out

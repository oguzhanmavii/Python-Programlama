from typer.testing import CliRunner
from . import app

runner= CliRunner()

def test_app():
    result=runner.invoke(app,["Daniel","--age",31])
    assert result.exit_code == 0
    assert "you are an adult" in result.stdout


def test_app_2():
    result= runner.invoke(app,["Gabriella","--age",29])
    assert result.exit_code == 0    
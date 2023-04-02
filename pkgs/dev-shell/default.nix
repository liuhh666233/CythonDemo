{ pkgs, mkShell, attr, ... }:

let
  customizedPython = pkgs.python3.withPackages (python-packages:
    with python-packages; [
      # For both Dev and Deploy
      click
      pytz
      redis
      tqdm
      loguru
      clickhouse-driver
      pydantic
      pyarrow
      pandas
      numpy
      graphviz
      prometheus_client
      nest-asyncio
      duckdb
      matplotlib
      numba
      # Dev only packages
      jupyterlab
      ipywidgets
      yapf
      pylint
      black
      snakeviz
      pyshark
      orjson
      cython_3
      line_profiler
      memory_profiler
      snakeviz
    ]);

  pythonIcon = "f3e2"; # https://fontawesome.com/v5.15/icons/python?style=brands

in mkShell rec {
  name = "Cython";

  packages = with pkgs; [ pkgs.poetry customizedPython pre-commit tshark];

  shellHook = ''
    export PS1="$(echo -e '\u${pythonIcon}') {\[$(tput sgr0)\]\[\033[38;5;228m\]\w\[$(tput sgr0)\]\[\033[38;5;15m\]} (${name}) \\$ \[$(tput sgr0)\]"
    export PYTHONPATH="$(pwd):$PYTHONPATH"
  '';

  buildInputs = [ attr ];
}

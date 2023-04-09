{ buildPythonApplication, pytestCheckHook, cython_3 }:

buildPythonApplication {
  pname = "CythonDemo";

  version = "1.0.0";

  srcs = ../..;

  propagatedBuildInputs = [ cython_3 ];

  checkInputs = [ pytestCheckHook ];

  doCheck = false;
}

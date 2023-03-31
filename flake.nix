{
  description = "A tool to monitor data-pipeline.";

  inputs = {
    nixpkgs.url =
      "github:NixOS/nixpkgs?rev=da26ae9f6ce2c9ab380c0f394488892616fc5a6a&tag=22.11";

    utils.url = "github:numtide/flake-utils";

  };

  outputs = { self, nixpkgs, ... }@inputs: { 
    overlays.dev = nixpkgs.lib.composeManyExtensions [
        ];
      } // inputs.utils.lib.eachSystem [ "x86_64-linux" ] (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          config.allowUnfree = true;
          overlays = [ self.overlays.dev ];
        };
      in {
        devShells.default = pkgs.callPackage ./pkgs/dev-shell { };
        packages.default =
          pkgs.python3Packages.callPackage ./pkgs/demo { };
        checks = if system == "x86_64-linux" then {
          run-unit-tests = self.packages."x86_64-linux".default;
        } else { };
      });
}

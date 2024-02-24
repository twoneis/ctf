{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, ... }@inputs: inputs.utils.lib.eachSystem [
    "x86_64-linux" "i686-linux" "aarch64-linux" "x86_64-darwin"
  ] (system: let
      pkgs = import nixpkgs {
        inherit system;
      };
      fhs = pkgs.buildFHSUserEnv {
        name = "ctf";

        targetPkgs = pkgs: with pkgs; [
          (cutter.withPlugins (pkgs: with pkgs; [cutterPlugins.rz-ghidra]))

          pwndbg

          (python3.withPackages (python-pkgs: with python311Packages; [
            python-lsp-server
            pwntools
          ]))

          ltrace
        ];

        runScript = ''
          zsh
        '';
      };
    in {
      devShells.default = fhs.env;
    });
}

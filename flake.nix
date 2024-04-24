{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    nixpkgs-old.url = "github:nixos/nixpkgs/nixos-23.11";
    nixpkgs-python.url = "github:cachix/nixpkgs-python";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, nixpkgs-old, nixpkgs-python, ... }@inputs: inputs.utils.lib.eachSystem [
    "x86_64-linux" "i686-linux" "aarch64-linux" "x86_64-darwin"
  ] (system: let
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
      };
      opkgs = import nixpkgs-old {
        inherit system;
        config.allowUnfree = true;
      };
      fhs = pkgs.buildFHSUserEnv {
        name = "ctf";

        targetPkgs = pkgs: with pkgs; [
          (opkgs.cutter.withPlugins (pkgs: with opkgs; [cutterPlugins.rz-ghidra]))

          pwndbg
          ltrace

          (python3.withPackages (python-pkgs: with python311Packages; [
            python-lsp-server
            pwntools
            pycryptodome
          ]))

          netcat-gnu
          postman

          clang-tools
          libllvm
          clang

          # for studsec-ctf/reversing/flag-packer
          nixpkgs-python.packages.x86_64-linux."3.7"
        ];

        runScript = ''
          zsh
        '';
      };
    in {
      devShells.default = fhs.env;
    });
}

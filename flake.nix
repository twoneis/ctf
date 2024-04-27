{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    nixpkgs-stable.url = "github:nixos/nixpkgs/nixos-23.11";
    nixpkgs-python.url = "github:cachix/nixpkgs-python";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, nixpkgs-stable, nixpkgs-python, ... }@inputs: inputs.utils.lib.eachSystem [
    "x86_64-linux" "i686-linux" "aarch64-linux" "x86_64-darwin"
  ] (system: let
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
      };
      stable-pkgs = import nixpkgs-stable {
        inherit system;
        config.allowUnfree = true;
      };
      fhs = pkgs.buildFHSUserEnv {
        name = "ctf";

        targetPkgs = pkgs: with pkgs; [
          (stable-pkgs.cutter.withPlugins (pkgs: with stable-pkgs; [cutterPlugins.rz-ghidra]))
          apktool

          pwndbg
          ltrace

          (python3.withPackages (python-pkgs: with python311Packages; [
            python-lsp-server
            pwntools
            pycryptodome
          ]))

          netcat-gnu
          postman
          wireshark

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

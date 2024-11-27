{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    nixpkgs-python.url = "github:cachix/nixpkgs-python";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, nixpkgs-python, ... }@inputs: inputs.utils.lib.eachSystem [
    "x86_64-linux" "i686-linux" "aarch64-linux" "x86_64-darwin"
  ] (system: let
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
      };

      mkXwlWrapper = import ./nix/xwl-wrapper.nix;

      fhs = pkgs.buildFHSUserEnv {
        name = "ctf";

        targetPkgs = pkgs: with pkgs; [
          # (pkgs.cutter.withPlugins (ps: with ps; [
          #   rz-ghidra
          # ]))
          (mkXwlWrapper {pkgs = pkgs; name = "ghidra";})
          apktool
          jadx

          gef
          pwndbg
          ltrace

          (python3.withPackages (python-pkgs: with python311Packages; [
            python-lsp-server
            pwntools
            pycryptodome
            angr
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
          fish
        '';
      };
    in {
      devShells.default = fhs.env;
    });
}

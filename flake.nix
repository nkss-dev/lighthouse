{
  description = "End the darkness";

  inputs = {
    flakey-devShells.url = "https://flakehub.com/f/GetPsyched/not-so-flakey-devshells/0.x.x.tar.gz";
    flakey-devShells.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = inputs@{ nixpkgs, flakey-devShells, ... }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      flakey-devShell-pkgs = flakey-devShells.outputs.packages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [
          pkgs.crudini
          pkgs.google-drive-ocamlfuse
          pkgs.python311Packages.aiohttp

          (flakey-devShell-pkgs.default.override { environments = [ "nix" "python" ]; })
          (flakey-devShell-pkgs.vscodium.override {
            environments = [ "nix" "python" ];
            extensions = with pkgs.vscode-extensions; [ tomoki1207.pdf ];
          })
        ];
      };
    };
}

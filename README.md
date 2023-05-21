# DarkSlateGray

VS Code theme based on them emacs theme of Jonathan Blow ([jblow](https://www.youtube.com/@jblow888)).
I didn't just want to name the theme after him so I named it after the closest named X11 color.

Generated using [Theme Studio](https://themes.vscode.one/theme/jjxyz/qR9dnyAe) where you can also fork and change it.

## Preview

![Preview](https://github.com/JaMo42/DarkSlateGray-theme/preview.png)

## Building

This is only required if you made any changes,
requires the [The Visual Studio Code Extension Manager](https://github.com/microsoft/vscode-vsce).

- Download the theme to `theme.json`.

- Optionally run `patch.py` to apply some changes:

    - Remove italic text styles (except for markdown)

    - Add colors for inlay hints and bracket highlight

    - Add some extra colors and change some of the generated colors

- Generate the package using `vsce package`

To install it go to the Extensions panel in VS Code, click on the 3 dots in the top right, and chose `Install from VSIX...`.

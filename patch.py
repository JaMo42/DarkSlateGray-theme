import json
from sys import argv

ADDITIONS = {
    "editorInlayHint.foreground": "#83735E",
    "editorInlayHint.background": "#0000",
    "editorInlayHint.parameterForeground": "#83735E",
    "editorInlayHint.parameterBackground": "#0000",
    "editorInlayHint.typeForeground": "#83735E",
    "editorInlayHint.typeBackground": "#0000",
    "editorBracketHighlight.foreground1": "#A99479",
    "editorBracketHighlight.foreground2": "#A99479",
    "editorBracketHighlight.foreground3": "#A99479",
}

SEMANTIC_TOKEN_COLORS = {
    "enumMember": "#8cde94",
    "formatSpecifier": "#6cd2b9",
    "operator": "#a08c73",
    #"method": "#c1d1e3",
    #"macro": "#c1d1e3",
    "parameter.declaration": "#c1d1e3",
    "variable.declaration": "#c1d1e3",
}

def _remove_italics(t):
    if t["settings"]["fontStyle"] == "italic" and "markdown" not in t["name"]:
        if len(t["settings"]) == 1:
            return True
        else:
            del t["settings"]["fontStyle"]

def _change_token_colors(t):
    if t["name"] == "Namespaces":
        t["settings"]["foreground"] = "d1b897"

def _dont_color_operators(t):
    if t["name"] in (
        "C operator assignment",
        "Other punctuation .c",
    ):
        return True
    is_op = False
    for i in t["scope"]:
        if i.startswith("keyword.operator"):
            if i.startswith("keyword.operator.sizeof"):
                t["settings"]["foreground"] = "#c1d1e3"
                return
            is_op = True
            break
    if not is_op:
        return
    #t["settings"]["foreground"] = "#d1b897"
    t["settings"]["foreground"] = "#A08C73"

def process_token_colors(theme):
    token_colors = theme["tokenColors"]
    # Filters may return `True` in which case the entire item will be deleted.
    # A return value is not required.
    filters = [
        _remove_italics,
        _change_token_colors,
        _dont_color_operators,
    ]
    for i in range(len(token_colors) - 1, -1, -1):
        t = token_colors[i]
        for f in filters:
            try:
                if f(t):
                    del token_colors[i]
            except KeyError:
                pass

def add_colors(theme):
    colors = theme["colors"]
    for k,v in ADDITIONS.items():
        colors[k] = v

def set_semantic_token_colors(theme):
    stc = theme["semanticTokenColors"]
    for k,v in SEMANTIC_TOKEN_COLORS.items():
        stc[k] = v

def add_c_preproc(theme):
    theme["tokenColors"].append({
        "name": "C Preprocessor",
        "scope": [
            "meta.preprocessor",
            "keyword.control.directive",
        ],
        "settings": {
            "foreground": "#8cde94"
        }
    })

def main():
    try:
        filename = argv[1]
    except:
        filename = "theme.json"
    theme = json.load(open(filename))
    process_token_colors(theme)
    add_colors(theme)
    set_semantic_token_colors(theme)
    add_c_preproc(theme)
    json.dump(theme, open(filename, 'w'))

if __name__ == "__main__":
    main()

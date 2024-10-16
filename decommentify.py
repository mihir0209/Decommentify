import sys
import os
COMMENT_FORMATS = {
    'python': {
        'single': ['#'],
        'multi': [('"""', '"""'), ("'''", "'''")]
    },
    'c_like': {
        'single': ['//'],
        'multi': [('/*', '*/')]
    },
    'sql': {
        'single': ['--'],
        'multi': [('/*', '*/')]
    },
    'html': {
        'multi': [('<!--', '-->')]
    },
    'ruby': {
        'single': ['#'],
        'multi': [('=begin', '=end')]
    },
    'haskell': {
        'single': ['--'],
        'multi': [('{-', '-}')]
    }
}
def get_language(file_name):
    ext = file_name.split('.')[-1]
    if ext in ['py']:
        return 'python'
    elif ext in ['c', 'cpp', 'h', 'java', 'js', 'cs']:
        return 'c_like'
    elif ext in ['sql']:
        return 'sql'
    elif ext in ['html', 'htm', 'xml']:
        return 'html'
    elif ext in ['rb']:
        return 'ruby'
    elif ext in ['hs']:
        return 'haskell'
    else:
        return None
def remove_comments(line, language, in_multiline_comment=False, in_docstring=False):
    in_single_quote = False
    in_double_quote = False
    result = []
    
    i = 0
    comment_formats = COMMENT_FORMATS.get(language, {})
    if 'docstring' in comment_formats and in_docstring:
        for start, end in comment_formats['docstring']:
            end_index = line.find(end)
            if end_index != -1:
                return line[end_index+len(end):], False, in_multiline_comment
        return "", True, in_multiline_comment
    if in_multiline_comment:
        for start, end in comment_formats.get('multi', []):
            end_index = line.find(end)
            if end_index != -1:
                return line[end_index+len(end):], False, in_docstring
        return "", True, in_docstring
    while i < len(line):
        char = line[i]
        if char == '"' and not in_single_quote:
            in_double_quote = not in_double_quote
        elif char == "'" and not in_double_quote:
            in_single_quote = not in_single_quote
        if in_single_quote or in_double_quote:
            result.append(char)
            i += 1
            continue
        for single in comment_formats.get('single', []):
            if language != 'sql' and line[i:i+len(single)] == single:
                return ''.join(result).rstrip(), False, False
            elif language == 'sql' and line[i:i+len(single)] == single:
                return ''.join(result).rstrip(), False, False
        for start, end in comment_formats.get('multi', []):
            if line[i:i+len(start)] == start:
                end_index = line.find(end, i + len(start))
                if end_index == -1:
                    return ''.join(result), True, False
                i = end_index + len(end) - 1
                break
        for start, end in comment_formats.get('docstring', []):
            if line[i:i+len(start)] == start:
                end_index = line.find(end, i + len(start))
                if end_index == -1:
                    return ''.join(result), False, True
                i = end_index + len(end) - 1
                break
        result.append(char)
        i += 1
    return ''.join(result).rstrip(), False, False
def decommentify(file_name):
    file_name = os.path.abspath(file_name)
    language = get_language(file_name)
    if language is None:
        print(f"Unsupported file type for: {file_name}")
        sys.exit(1)
    with open(file_name) as f:
        content = f.readlines()
    with open(file_name, 'w') as file:
        in_multiline_comment = False
        in_docstring = False
        for line in content:
            clean_line, in_multiline_comment, in_docstring = remove_comments(line, language, in_multiline_comment, in_docstring)
            if clean_line:
                file.write(clean_line + '\n')
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decommentify.py <filename>")
        sys.exit(1)
    file_name = sys.argv[1]
    decommentify(file_name)

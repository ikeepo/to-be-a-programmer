# Bash
# Setup Shell 
[craftdog](https://github.com/craftzdog/dotfiles-public)
# Usage
- `exec "$@"`

`exec` would replace the current shell;

`$@` means all the positional arguments passed to the script.

##### `$1`
positional arguments of the scripts: `$0 $1 $2` 

##### `-z string`
return true if the length of the string is [ zero ](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html);
##### `$(date +'%Y-%m-%d')`

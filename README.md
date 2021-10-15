## Git Interface for Python
Welcome to the git repository for the Python-Git Interface. The GitInterface class provides an easy-to-use function set for dealing with the Git Bash from Python.

## Contents
|File            |Description                   |
|---             |---                           |
|README          |this file                     |
|git_interface.py|houses the GitInterface class.|

## Example
```
from git_interface import GitInterface

g = GitInterface('github', 'C:/Users/repository_path')
g.commit('Bug fixes')
g.push('master')
```

## Git Interface for Python
Welcome to the git repository for the Python-Git Interface. The GitInterface class provides an easy-to-use function set for dealing with the Git Bash from Python.



GitInterface makes tasks that require upload/download with git easy to automate using Python. GitInterface provides support for basic git commands with more on the way!

To use this module, you should have the git bash downloaded and a repository ready to be automated. Now you can just import the class and git started.

## Contents
|File            |Description                   |
|---             |---                           |
|README          |this file                     |
|git_interface.py|houses the GitInterface class.|

## Example
```
from git_interface import GitInterface

g = GitInterface('C:/Users/local_repository_path')
g.commit('Bug fixes')
g.push('master')
```

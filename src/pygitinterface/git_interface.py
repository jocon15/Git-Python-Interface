"""
This file is part of Git-Python-Interface which is released under the MIT License.
See file LICENSE.txt or go to https://github.com/jocon15/Git-Python-Interface/blob/master/LICENSE for full license details.
"""
import subprocess


class GitInterface:

    def __init__(self, cwd, repo_cite='github'):
        self.repo_cite = repo_cite
        self.cwd = cwd

    def add(self, tag='-A'):
        # can be file or a switch
        tag = str(tag)
        if not tag:
            raise Exception('Please enter a file name or a switch')
        self._create_bat(f'git add {tag}')
        self._execute_bat()

    def branch(self, src_branch_name, dst_branch_name):
        src_branch_name = str(src_branch_name)
        dst_branch_name = str(dst_branch_name)
        if not src_branch_name:
            raise Exception('Please enter a branch name.')
        if not dst_branch_name:
            raise Exception('Please enter a new branch name.')
        self._create_bat(f'git branch {src_branch_name} {dst_branch_name}')
        self._execute_bat()

    def checkout(self, branch_name):
        branch_name = str(branch_name)
        if not branch_name:
            raise Exception('Please enter a branch name')
        self._create_bat('git checkout{branch_name}')
        self._execute_bat()

    def commit(self, message=None):
        message = str(message)
        self._create_bat(f'git commit -m {message}')
        self._execute_bat()

    def pull(self, branch_name):
        if branch_name:
            self._create_bat('git pull{self.repo_cite} {branch_name}')
            self._execute_bat()
        else:
            self._create_bat('git pull')
            self._execute_bat()

    def push(self, branch_name):
        if branch_name:
            self._create_bat(f'git push {self.repo_cite} {branch_name}')
            self._execute_bat()
        else:
            self._create_bat('git push')
            self._execute_bat()

    def rebase(self, rebase_branch_name):
        rebase_branch_name = str(rebase_branch_name)
        if not rebase_branch_name:
            raise Exception('Please enter a branch name')
        self._create_bat(f'git rebase {rebase_branch_name}')
        self._execute_bat()

    def status(self):
        self._create_bat('git status')
        self._execute_bat

    def _create_bat(self, args):
        """Create subbat from args"""
        if not args:
            raise Exception('No args passed.')
        lines = []
        lines.append(f'cd {self.cwd}\n')
        lines.append(f'call {args}')
        with open('commands.bat', 'w+') as file:
            file.writelines(lines)

    def _execute_bat(self):
        subprocess.Popen(['commands.bat'], shell=False)

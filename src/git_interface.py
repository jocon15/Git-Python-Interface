"""
This file is part of Git-Python-Interface which is released under the MIT License.
See file LICENSE.txt or go to https://github.com/jocon15/Git-Python-Interface/blob/master/LICENSE for full license details.
"""
import subprocess


class GitInterface:

    def __init__(self, cwd, repo_cite='github'):
        self.repo_cite = repo_cite
        self.cwd = cwd

    def push(self, branch):
        if branch:
            self._create_process(['git', 'push', self.repo_cite, branch])
        else:
            self._create_process(['git', 'push'])

    def pull(self, branch):
        if not branch:
            self._create_process(['git', 'pull', self.repo_cite, branch])
        else:
            self._create_process(['git', 'pull'])

    def status(self):
        self._create_process(['git', 'status'])

    def add(self, tag='-A'):
        # can be file or a switch
        if tag == '-A':
            self._create_process(['git', 'add', tag])
        else:
            raise NotImplementedError

    def commit(self, message=None):
        message = str(message)
        self._create_process(['git', 'commit', '-m', f'{message}'])

    def rebase(self):
        raise NotImplementedError

    def branch(self, src_branch_name, dst_branch_name):
        src_branch_name = str(src_branch_name)
        dst_branch_name = str(dst_branch_name)
        if not src_branch_name:
            raise Exception('Please enter a branch name.')
        if not dst_branch_name:
            raise Exception('Please enter a new branch name.')
        self._create_process(
            ['git', 'branch', src_branch_name, dst_branch_name])

    def _create_process(self, args):
        """Create subprocess from args"""
        if type(args) != list:
            raise Exception('Args must be a list.')
        if not args:
            raise Exception('No args passed.')
        subprocess.Popen(args, cwd=self.cwd, shell=False)

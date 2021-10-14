import subprocess


class GitInterface:

    def __init__(self, repo_name, cwd):
        self.repo_name = repo_name
        self.cwd = cwd

    def push(self, origin=None, branch=None):
        if (origin and not branch) or (not origin and branch):
            raise Exception(
                'You must enter both origin and a branch or neither.')
        if origin and branch:
            self._create_process(['git', 'push', origin, branch])
        else:
            self._create_process(['git', 'push'])

    def pull(self, origin=None, branch=None):
        if (origin and not branch) or (not origin and branch):
            raise Exception(
                'You must enter both origin and a branch or neither.')
        if origin and branch:
            self._create_process(['git', 'pull', origin, branch])
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
        pass

    def branch(self, src_branch_name, dst_branch_name):
        src_branch_name = str(src_branch_name)
        dst_branch_name = str(dst_branch_name)
        if not src_branch_name:
            raise Exception('Please enter a branch name.')
        if not dst_branch_name:
            raise Exception('Please enter a new branch name.')
        self._create_process(['git', 'branch', src_branch_name, dst_branch_name])

    def _create_process(self, args):
        """Create subprocess from args"""
        if type(args) != list:
            raise Exception('Args must be a list.')
        if not args:
            raise Exception('No args passed.')
        subprocess.Popen(args, cwd=self.cwd, shell=False)

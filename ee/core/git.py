from sh import git, ErrorReturnCode
import os
from ee.core.logging import Log


class EEGit:
    """Intialization of core variables"""
    def ___init__():
        # TODO method for core variables
        pass

    def add(self, paths, msg="Intializating"):
        for path in paths:
            global git
            git = git.bake("--git-dir={0}/.git".format(path),
                           "--work-tree={0}".format(path))
            if os.path.isdir(path):
                if not os.path.isdir(path+"/.git"):
                    try:
                        Log.debug(self, "EEGit: git init at {0}"
                                  .format(path))
                        git.init(path)
                    except ErrorReturnCode as e:
                        Log.error(self, "Unable to git init at {0}"
                                  .format(path))
                        Log.error(self, "{0}".format(e))
                        sys.exit(1)
                status = git.status("-s")
                if len(status.splitlines()) > 0:
                    try:
                        Log.debug(self, "EEGit: git commit at {0}"
                                  .format(path))
                        git.add("--all")
                        git.commit("-am {0}".format(msg))
                    except ErrorReturnCode as e:
                        Log.error(self, "Unable to git commit at {0} "
                                  .format(path))
                        Log.debug(self, "{0}".format(e))
                        sys.exit(1)
            else:
                Log.debug(self, "EEGit: Path {0} not present".format(path))

    def checkfilestatus(self, repo, filepath):
        global git
        git = git.bake("--git-dir={0}/.git".format(repo),
                       "--work-tree={0}".format(repo))
        status = git.status("-s", "{0}".format(filepath))
        if len(status.splitlines()) > 0:
            return True
        else:
            return False

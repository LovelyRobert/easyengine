"""EasyEngine file utils core classes."""
import shutil
import os
import sys
import glob
import shutil
import fileinput
from ee.core.logging import Log


class EEFileUtils():
    """Method to operate on files"""
    def __init__():
        pass

    def remove(self, filelist):
        for file in filelist:
            if os.path.isfile(file):
                Log.info(self, "Removing "+os.path.basename(file)+" ...")
                os.remove(file)
                Log.debug(self, 'file Removed')
            if os.path.isdir(file):
                try:
                    Log.info(self, "Removing "+os.path.basename(file)+"...")
                    shutil.rmtree(file)
                except shutil.Error as e:
                    Log.debug(self, "{err}".format(err=str(e.reason)))
                    Log.error(self, 'Unable to Remove file ')

    def create_symlink(self, paths, errormsg=''):
        src = paths[0]
        dst = paths[1]
        if not os.path.islink(dst):
            try:
                os.symlink(src, dst)
            except Exception as e:
                Log.debug(self, "{0}{1}".format(e.errno, e.strerror))
                Log.error(self, "Unable to create symbolic link ...\n ")
        else:
            Log.debug(self, "Destination: {0} exists".format(dst))

    def remove_symlink(self, filepath):
        try:
            os.unlink(filepath)
        except Exception as e:
            Log.debug(self, "{0}".format(e))
            Log.error(self, "Unable to reomove symbolic link ...\n")

    def copyfile(self, src, dest):
        try:
            shutil.copy2(src, dest)
        except shutil.Error as e:
            Log.debug(self, "{0}".format(e))
            Log.error(self, 'Unable to copy file from {0} to {1}'
                      .format(src, dest))
        except IOError as e:
            Log.debug(self, "{e}".format(e.strerror))
            Log.error(self, "Unable to copy file from {0} to {1}"
                      .fromat(src, dest))

    def searchreplace(self, fnm, sstr, rstr):
        try:
            for line in fileinput.input(fnm, inplace=True):
                print(line.replace(sstr, rstr), end='')
            fileinput.close()
        except Exception as e:
            Log.debug(self, "{0}".format(e))
            Log.error(self, "Unable to search {0} and replace {1} {2}"
                      .format(fnm, sstr, rstr))

    def mvfile(self, src, dst):
        try:
            shutil.move(src, dst)
        except shutil.Error as e:
            Log.debug(self, "{err}".format(err=str(e.reason)))
            Log.error(self, 'Unable to move file from {0} to {1}'
                      .format(src, dst))

    def chdir(self, path):
        try:
            os.chdir(path)
        except OSError as e:
            Log.debug(self, "{err}".format(err=e.strerror))
            Log.error(self, 'Unable to Change Directory {0}'.format(path))

    def chown(self, path, user, group, recursive=False):
        try:
            if recursive:
                for root, dirs, files in os.walk(path):
                    for d in dirs:
                        shutil.chown(os.path.join(root, d), user=user,
                                     group=group)
                    for f in files:
                        shutil.chown(os.path.join(root, f), user=user,
                                     group=group)
            else:
                shutil.chown(path, user=user, group=group)
        except shutil.Error as e:
            Log.debug(self, "{0}".format(e))
            Log.error(self, "Unable to change owner : {0}".format(path))
        except Exception as e:
            Log.debug(self, "{0}".format(e))
            Log.error(self, "Unable to change owner : {0} ".format(path))

    def chmod(self, path, perm, recursive=False):
        try:
            if recursive:
                for root, dirs, files in os.walk(path):
                    for d in dirs:
                        os.chmod(os.path.join(root, d), perm)
                    for f in files:
                        os.chmod(os.path.join(root, f), perm)
            else:
                os.chmod(path, perm)
        except OSError as e:
            Log.debug(self, "{0}".format(e.strerror))
            Log.error(self, "Unable to change owner : {0}".format(path))

    def mkdir(self, path):
        try:
            os.makedirs(path)
        except OSError as e:
            Log.debug(self, "{0}".format(e.strerror))
            Log.error(self, "Unable to create directory {0} ".format(path))

    def isexist(self, path):
        try:
            if os.path.exists(path):
                return (True)
            else:
                return (False)
        except OSError as e:
            Log.debug(self, "{0}".format(e.strerror))
            Log.error(self, "Unable to check path {0}".format(path))

    def grep(self, fnm, sstr):
        try:
            for line in open(fnm):
                if sstr in line:
                    return line
        except OSError as e:
            Log.debug(self, "{0}".format(e.strerror))
            Log.error(self, "Unable to Search string {0} in {1}"
                      .format(sstr, fnm))

    def rm(self, path):
        if EEFileUtils.isexist(self, path):
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
            except shutil.Error as e:
                Log.debug(self, "{0}".format(e))
                Log.error(self, "Unable to remove directory : {0} "
                          .format(path))
            except OSError as e:
                Log.debug(self, "{0}".format(e))
                Log.error(self, "Unable to remove file  : {0} "
                          .format(path))
